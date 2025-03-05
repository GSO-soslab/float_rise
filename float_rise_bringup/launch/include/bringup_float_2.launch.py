import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, PythonExpression
import time


def generate_launch_description():
    robot_bringup = 'float_rise_bringup'

    vehicle_name = 'float_2'

    description = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory(robot_bringup), 
            'launch', 'include', vehicle_name, 'description.launch.py')]),
        # launch_arguments = {'arg_robot_name': arg_robot_name}.items()  
    )

    localization = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory(robot_bringup), 
            'launch', 'include', vehicle_name, 'localization.launch.py')]),
        # launch_arguments = {'arg_robot_name': arg_robot_name}.items()  
    )
    
    mvp_control = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory(robot_bringup), 
            'launch', 'include', vehicle_name, 'mvp_control.launch.py')]),
        # launch_arguments = {'arg_robot_name': arg_robot_name}.items()  
    )

    # mvp_mission = IncludeLaunchDescription(
    #     PythonLaunchDescriptionSource([os.path.join(get_package_share_directory(robot_bringup), 'launch','include','mvp_mission.launch.py')]),
    #     # launch_arguments = {'arg_robot_name': arg_robot_name}.items()  
    # )   

    return LaunchDescription([
        description,
        localization,
        mvp_control,
        # mvp_mission,
    ])    