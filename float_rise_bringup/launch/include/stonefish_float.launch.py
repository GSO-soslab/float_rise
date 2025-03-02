import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument

def generate_launch_description():

    # =================================================== #
    # parameters
    # =================================================== #
    robot_bringup = 'float_rise_bringup'
    robot_param_path = os.path.join(
        get_package_share_directory(robot_bringup),
        'config'
    )
    stonefish_driver_param_file = os.path.join(
        robot_param_path, 
        'new_sim_params.yaml'
    ) 

    # =================================================== #
    # passed config
    # =================================================== #
    robot_name = LaunchConfiguration('arg_robot_name')
    arg_robot = DeclareLaunchArgument(
        'arg_robot_names',
        default_value='float_rise'
    )

    world_frame = LaunchConfiguration('arg_world_frame')
    arg_world_frame = DeclareLaunchArgument(
        'arg_world_frame',
        default_value='float_rise/world'
    )

    imu_frame = LaunchConfiguration('arg_imu_frame')
    arg_sensor_frame = DeclareLaunchArgument(
        'arg_imu_frame',
        default_value='float_rise/imu_sf'
    )
    
    # =================================================== #
    # launch the stonefish sensor convertor
    # =================================================== #
    return LaunchDescription([

        # stonefish thruster convector
        Node(
            package="world_of_stonefish",
            executable="thruster_driver_node",
            namespace=robot_name,
            name="thruster_driver_node",
            # prefix=['stdbuf -o L'],
            # output="screen",
            parameters=[stonefish_driver_param_file]
        ),

        # stonefish IMU convector
        Node(
            package="world_of_stonefish",
            executable="imu_driver_node",
            namespace=robot_name,
            name="imu_driver_node",
            remappings=[
                    ('imu_in/data', 'imu/stonefish/data'),
                    ('imu_out/data', 'imu/data'),
            ],
            parameters=[
                {'frame_id': imu_frame},
                stonefish_driver_param_file
            ]
        ),

        # stonefish DVL convector
        Node(
            package="world_of_stonefish",
            executable="dvl_driver_node",
            namespace=robot_name,
            name="dvl_driver_node",
            parameters=[stonefish_driver_param_file]
        ),

        # stonefish pressure convector
        Node(
            package="world_of_stonefish",
            executable="pressure_sensor_node",
            namespace=robot_name,
            name="pressure_sensor_node",
            parameters=[
                {'frame_id': world_frame}]
        )

        # stonefish usbl convector
        # Node(
        #     package="world_of_stonefish",
        #     executable="usbl_driver_node",
        #     namespace=robot_name,
        #     name="usbl_driver_node",
        #     # parameters=[
        #         # {'frame_id': world_frame}
        #         # ]
        # )

    ])