
from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node
import os
import yaml
# import xacro
from launch.substitutions import EnvironmentVariable
import pathlib
import launch.actions
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
from launch_ros.descriptions import ParameterValue
from setuptools import Command

def generate_launch_description():
    robot_name = 'float_rise'
    # robot_description = robot_name + '_description'

    path_to_urdf = os.path.join( 
        get_package_share_directory('float_rise_description'), 'urdf', 'base.urdf' )
    with open(path_to_urdf, 'r') as infp:
        robot_desc = infp.read()

    rviz_config_dir = os.path.join( 
        get_package_share_directory('float_rise_description'), 'config', 'rviz.rviz' )
    rqt_config_dir = os.path.join( 
        get_package_share_directory('float_rise_description'), 'config', 'rqt.perspective' )

    return LaunchDescription([
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            arguments=['-d', [rviz_config_dir]],
        ),

        Node(package="rqt_gui", 
             executable="rqt_gui", 
             name="rqt", 
             arguments=["--perspective-file", rqt_config_dir],
        ),

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            namespace=robot_name,
            # output='screen',
            parameters=[{'robot_description' : robot_desc},
                        {'frame_prefix': robot_name +'/'}],
        ),

        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='world2ned',
            arguments = ["0.0", "0.0", "0.0", "1.571", "0.0", "3.1415", robot_name+'/world', robot_name+'/world_ned']    
        ),
])
