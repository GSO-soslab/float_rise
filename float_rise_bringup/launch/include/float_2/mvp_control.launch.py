import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.actions import TimerAction


def generate_launch_description():
    robot_name = 'float_rise_2'
    robot_bringup = 'float_rise_bringup'
    robot_config = 'float_rise_config'
    vehicle_name = 'float_2'

    robot_param_path = os.path.join(
        get_package_share_directory(robot_bringup),
        'config',
        vehicle_name
    )
    robot_config_path = os.path.join(
        get_package_share_directory(robot_config),
        'mvp_control_config',
        vehicle_name
    )

    mvp_control_param_file = os.path.join(robot_param_path, 'mvp_control.yaml') 
    mvp_control_config_file = os.path.join(robot_config_path, 'config.yaml') 

    return LaunchDescription([

        TimerAction(period=5.0,
            actions=[
                    Node(
                        package="mvp_control",
                        executable="mvp_control_ros_node",
                        namespace=robot_name,
                        name="mvp_control_ros_node",
                        prefix=['stdbuf -o L'],
                        # prefix=['xterm -e gdb -ex run --args'],
                        output="screen",
                        parameters=[
                            {'config_file': mvp_control_config_file},
                            {'tf_prefix': robot_name},
                            {'odometry_source': '/'+ robot_name + '/odometry/filtered'},
                            mvp_control_param_file
                            ]
                        )
            ])
        
])