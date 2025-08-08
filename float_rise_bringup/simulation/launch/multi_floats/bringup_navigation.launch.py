import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, PythonExpression
import time


def generate_launch_description():
    robot_name = LaunchConfiguration('robot_name')

    robot_bringup = 'float_rise_bringup'

    description = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory(robot_bringup), 
            'launch', 'multi_floats', 'description.launch.py')]),

        launch_arguments = {
            'robot_name' : robot_name,
            'description_delay' : '0.0',
        }.items()   
    )

    localization = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory(robot_bringup), 
            'launch', 'multi_floats', 'localization.launch.py')]),

        launch_arguments = {
            'robot_name' : robot_name,
            'localization_delay' : '1.0',
        }.items()   
    )
    
    mvp_control = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory(robot_bringup), 
            'launch', 'multi_floats', 'mvp_control.launch.py')]),

        launch_arguments = {
            'robot_name' : robot_name,
            'control_delay' : '2.0',
        }.items()   
    )

    mvp_mission = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory(robot_bringup), 
            'launch', 'multi_floats', 'mvp_mission.launch.py')]),

        launch_arguments = {
            'robot_name' : robot_name,
            'mission_delay' : '3.0',
        }.items()                
    )   

    return LaunchDescription([
        # Decalre arguments
        DeclareLaunchArgument(
            'robot_name', default_value = 'my_robot'            
        ),

        description,
        localization,
        mvp_control,
        mvp_mission,
    ])    