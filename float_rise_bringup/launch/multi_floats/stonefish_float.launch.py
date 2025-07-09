import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription, LaunchContext
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument, OpaqueFunction
from launch_ros.substitutions import FindPackageShare

# This function will be executed at launch time
def launch_setup(context: LaunchContext):
    """
    This function resolves launch configurations and constructs the node
    with the final, concrete paths.
    """
    # 1. Resolve the substitutions into plain Python strings
    # robot_name_str = context.perform_substitution(LaunchConfiguration('arg_robot_name'))

    # 3. Create the Node objects
    robot_name_prefix = ['/', LaunchConfiguration('arg_robot_name'), '_', LaunchConfiguration('arg_robot_id')]
    robot_name = [LaunchConfiguration('arg_robot_name'), '_', LaunchConfiguration('arg_robot_id')]

    # stonefish thruster convector
    thruster_convector = Node(
        package="world_of_stonefish",
        executable="thruster_driver_node",
        namespace=robot_name,
        name="thruster_driver_node",
        # prefix=['stdbuf -o L'],
        # output="screen",
        parameters=[
            {'thruster_pub_topic': robot_name_prefix + ['/stonefish/thruster_command']},
            {'thruster_length': 2},
            {'thruster_sub_topics': [
                robot_name_prefix + ['/control/thruster/port'],
                robot_name_prefix + ['/control/thruster/stbd']
            ]},
        ]
    )

    # stonefish IMU convector
    imu_convector = Node(
        package="world_of_stonefish",
        executable="imu_driver_node",
        namespace=robot_name,
        name="imu_driver_node",
        remappings=[
                ('imu_in/data', 'imu/stonefish/data'),
                ('imu_out/data', 'imu/data'),
        ],
        parameters=[
            {'frame_id': robot_name + ['/imu_sf']},
            {'roll_offset': 3.1415926},
            {'pitch_offset': 0.0},
            {'yaw_offset': 1.5707},
            {'roll_reverse': 1.0},
            {'pitch_reverse': -1.0},
            {'yaw_reverse': -1.0},
        ]
    )

    # stonefish DVL convector
    dvl_convector = Node(
        package="world_of_stonefish",
        executable="dvl_driver_node",
        namespace=robot_name,
        name="dvl_driver_node",
        parameters=[
            {'dvl_in': robot_name_prefix + ['/dvl/stonefish/raw']},
            {'dvl_out': robot_name_prefix + ['/dvl/twist']},
            {'dvl_alt_out': robot_name_prefix + ['/dvl/altitude']},
        ]
    )

    # stonefish pressure convector
    pressure_convector = Node(
        package="world_of_stonefish",
        executable="pressure_sensor_node",
        namespace=robot_name,
        name="pressure_sensor_node",
        parameters=[
            {'frame_id': robot_name + ['/world']}]
    )

    ### DEBUG:
    # print(f"--- robot_id: {robot_name_prefix} ---")
    # print(f"--- robot_name: {robot_name} ---")

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