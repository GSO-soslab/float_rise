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

    # =================================================== #
    # bringup everything related to stonefish simulator
    # =================================================== #

    simulation = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory(robot_bringup), 
            'launch', 'include', 'stonefish.launch.py')]),
        # launch_arguments = {'arg_robot_name': arg_robot_name}.items()    
    )    

    # =================================================== #
    # bringup everything related to ros setup for float 1
    # =================================================== #

    # =================================================== #
    # bringup everything related to ros setup for float 2
    # =================================================== #

    return LaunchDescription([
        simulation,
    ])    