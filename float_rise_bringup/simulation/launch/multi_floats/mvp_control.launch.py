from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch.substitutions import PythonExpression
from launch.actions import SetEnvironmentVariable
from launch.actions import TimerAction
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from pathlib import Path
import os

def generate_launch_description():

    # Node argument
    robot_name = LaunchConfiguration('robot_name')
    control_delay = LaunchConfiguration('control_delay')

    # Node param
    control_param_file = os.path.join(
        get_package_share_directory('float_rise_bringup'),
        'config',
        'float',
        'mvp_control.yaml'
    )

    control_config_file = os.path.join(
        get_package_share_directory('float_rise_config'),
        'mvp_control_config',
        'float',
        'config.yaml'
    )

    # mvp control node
    node = Node(
        package="mvp_control",
        executable="mvp_control_ros_node",
        namespace=robot_name,
        name="mvp_control_ros_node",
        prefix=['stdbuf -o L'],
        # prefix=['xterm -e gdb -ex run --args'],
        output="screen",
        parameters=[
            {'config_file': control_config_file},
            {'tf_prefix': robot_name},
            {'odometry_source': ['/', robot_name, '/odometry/filtered']},
            control_param_file
        ],
        emulate_tty=True        
    )
        
    return LaunchDescription([

        # Decalre arguments
        DeclareLaunchArgument(
            'robot_name', default_value = 'my_robot'            
        ),

        DeclareLaunchArgument(
            'control_delay', default_value = '0.0'            
        ),

        # Delay the node if needed
        TimerAction(
            period=PythonExpression([control_delay]),
            actions=[node]
        ),
    ])
