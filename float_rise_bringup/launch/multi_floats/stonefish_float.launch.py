import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription, LaunchContext
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument, LogInfo, OpaqueFunction
from launch_ros.substitutions import FindPackageShare

# This function will be executed at launch time
def launch_setup(context: LaunchContext):
    """
    This function resolves launch configurations and constructs the node
    with the final, concrete paths.
    """
    # 1. Resolve the substitutions into plain Python strings
    robot_id_str = context.perform_substitution(LaunchConfiguration('arg_robot_id'))
    robot_name_str = context.perform_substitution(LaunchConfiguration('arg_robot_name'))
    pkg_share_path = context.perform_substitution(FindPackageShare('float_rise_bringup'))

    # 2. e.g., 'float_0', the folder name contains param for each robot
    robot_param = f'float_{robot_id_str}' 
    
    stonefish_driver_param_file = os.path.join(
        pkg_share_path,
        'config',
        robot_param,
        'sim_params.yaml'
    )

    # 3. Create the Node objects

    # stonefish thruster convector
    thruster_convector = Node(
        package="world_of_stonefish",
        executable="thruster_driver_node",
        namespace=[robot_name_str, '_', LaunchConfiguration('arg_robot_id')],
        name="thruster_driver_node",
        # name=['thruster_driver_', robot_name_str, '_', LaunchConfiguration('arg_robot_id')],
        # prefix=['stdbuf -o L'],
        # output="screen",
        parameters=[stonefish_driver_param_file]
    )

    # stonefish IMU convector
    imu_convector = Node(
        package="world_of_stonefish",
        executable="imu_driver_node",
        namespace=[robot_name_str, '_', LaunchConfiguration('arg_robot_id')],
        name="imu_driver_node",
        # name=['imu_driver_', robot_name_str, '_', LaunchConfiguration('arg_robot_id')],
        remappings=[
                ('imu_in/data', 'imu/stonefish/data'),
                ('imu_out/data', 'imu/data'),
        ],
        parameters=[
            {'frame_id': [robot_name_str, '_', LaunchConfiguration('arg_robot_id'), '/imu_sf']},
            stonefish_driver_param_file
        ]
    )

    # stonefish DVL convector
    dvl_convector = Node(
        package="world_of_stonefish",
        executable="dvl_driver_node",
        namespace=[robot_name_str, '_',  LaunchConfiguration('arg_robot_id')],
        name="dvl_driver_node",
        # name=['dvl_driver_', robot_name_str, '_', LaunchConfiguration('arg_robot_id')],
        parameters=[stonefish_driver_param_file]
    )

    # stonefish pressure convector
    pressure_convector = Node(
        package="world_of_stonefish",
        executable="pressure_sensor_node",
        namespace=[robot_name_str, '_', LaunchConfiguration('arg_robot_id')],
        name="pressure_sensor_node",
        # name=['pressure_sensor_', robot_name_str, '_', LaunchConfiguration('arg_robot_id')],
        parameters=[
            {'frame_id': [robot_name_str, '_',  LaunchConfiguration('arg_robot_id'), '/world']}]
    )

    ### DEBUG:
    # print(f"--- Loading parameters from: {stonefish_driver_param_file} ---")
    # print(f"--- robot_id: {robot_id_str} ---")
    # print(f"--- robot_name: {robot_name_str} ---")

    # 4. An OpaqueFunction must return a list of launch actions/nodes
    return [thruster_convector, imu_convector, dvl_convector, pressure_convector]


def generate_launch_description():
    # Declare the argument so it's available to the OpaqueFunction
    arg_robot_id = DeclareLaunchArgument(
        'arg_robot_id',
        default_value='0',
        description='The ID of the robot'
    )

    arg_robot_name = DeclareLaunchArgument(
        'arg_robot_name',
        default_value='float',
        description='The name the robot'
    )

    # The OpaqueFunction action that will call our setup function
    launch_nodes_action = OpaqueFunction(function=launch_setup)

    return LaunchDescription([
        arg_robot_id,
        arg_robot_name,
        launch_nodes_action
    ])