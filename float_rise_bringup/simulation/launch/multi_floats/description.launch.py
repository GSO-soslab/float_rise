# description.launch.py (CORRECTED for GroupAction method)

import os
from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.actions import TimerAction
from launch.substitutions import LaunchConfiguration, PythonExpression

def generate_launch_description():
    # These LaunchConfigurations get their values from the parent file.
    robot_name = LaunchConfiguration('robot_name')
    description_delay = LaunchConfiguration('description_delay')

    path_to_urdf = os.path.join( 
        get_package_share_directory('float_rise_description'), 'urdf', 'float', 'base.urdf' )
    with open(path_to_urdf, 'r') as infp:
        robot_desc = infp.read()

    node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        namespace=robot_name,
        parameters=[{'robot_description' : robot_desc},
                    {'frame_prefix': [robot_name, '/']}],
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            'robot_name', default_value = 'my_robot'            
        ),

        DeclareLaunchArgument(
            'description_delay', default_value = '0.0'            
        ),

        TimerAction(
            period=PythonExpression([description_delay]), # This will now work correctly
            actions=[node]
        ),
    ])