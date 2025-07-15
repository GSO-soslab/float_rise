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
            'launch', 'include', 'bringup_stonefish.launch.py')]),
        # launch_arguments = {'arg_robot_name': arg_robot_name}.items()    
    )    

    # =================================================== #
    # bringup everything related to ros setup for floats
    # =================================================== #

    # Float No. 1
    float_1 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory(robot_bringup), 
            'launch', 'include', 'bringup_float_1.launch.py')]),
        # launch_arguments = {'arg_robot_name': arg_robot_name}.items()    
    )   

    # Float No. 2
    float_2 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory(robot_bringup), 
            'launch', 'include', 'bringup_float_2.launch.py')]),
        # launch_arguments = {'arg_robot_name': arg_robot_name}.items()    
    ) 

    # Float No. 3
    float_3 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory(robot_bringup), 
            'launch', 'include', 'bringup_float_3.launch.py')]),
        # launch_arguments = {'arg_robot_name': arg_robot_name}.items()    
    ) 

    # Float No. 4
    float_4 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory(robot_bringup), 
            'launch', 'include', 'bringup_float_4.launch.py')]),
        # launch_arguments = {'arg_robot_name': arg_robot_name}.items()    
    ) 

    # Float No. 5
    float_5 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory(robot_bringup), 
            'launch', 'include', 'bringup_float_5.launch.py')]),
        # launch_arguments = {'arg_robot_name': arg_robot_name}.items()    
    ) 

    # Float No. 6
    float_6 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory(robot_bringup), 
            'launch', 'include', 'bringup_float_6.launch.py')]),
        # launch_arguments = {'arg_robot_name': arg_robot_name}.items()    
    ) 

    # Float No. 7
    float_7 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory(robot_bringup), 
            'launch', 'include', 'bringup_float_7.launch.py')]),
        # launch_arguments = {'arg_robot_name': arg_robot_name}.items()    
    ) 

    # Float No. 8
    float_8 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory(robot_bringup), 
            'launch', 'include', 'bringup_float_8.launch.py')]),
        # launch_arguments = {'arg_robot_name': arg_robot_name}.items()    
    ) 

    # # Float No. 9
    # float_9 = IncludeLaunchDescription(
    #     PythonLaunchDescriptionSource([
    #         os.path.join(get_package_share_directory(robot_bringup), 
    #         'launch', 'include', 'bringup_float_9.launch.py')]),
    #     # launch_arguments = {'arg_robot_name': arg_robot_name}.items()    
    # ) 

    # # Float No. 10
    # float_10 = IncludeLaunchDescription(
    #     PythonLaunchDescriptionSource([
    #         os.path.join(get_package_share_directory(robot_bringup), 
    #         'launch', 'include', 'bringup_float_10.launch.py')]),
    #     # launch_arguments = {'arg_robot_name': arg_robot_name}.items()    
    # ) 

    # # Float No. 11
    # float_11 = IncludeLaunchDescription(
    #     PythonLaunchDescriptionSource([
    #         os.path.join(get_package_share_directory(robot_bringup), 
    #         'launch', 'include', 'bringup_float_11.launch.py')]),
    #     # launch_arguments = {'arg_robot_name': arg_robot_name}.items()    
    # ) 

    # # Float No. 12
    # float_12 = IncludeLaunchDescription(
    #     PythonLaunchDescriptionSource([
    #         os.path.join(get_package_share_directory(robot_bringup), 
    #         'launch', 'include', 'bringup_float_12.launch.py')]),
    #     # launch_arguments = {'arg_robot_name': arg_robot_name}.items()    
    # ) 

    # # Float No. 13
    # float_13 = IncludeLaunchDescription(
    #     PythonLaunchDescriptionSource([
    #         os.path.join(get_package_share_directory(robot_bringup), 
    #         'launch', 'include', 'bringup_float_13.launch.py')]),
    #     # launch_arguments = {'arg_robot_name': arg_robot_name}.items()    
    # ) 

    # =================================================== #
    # bringup visualization
    # =================================================== #

    vis = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory(robot_bringup), 
            'launch', 'include', 'bringup_visualization.launch.py')]),
        # launch_arguments = {'arg_robot_name': arg_robot_name}.items()    
    )    

    return LaunchDescription([
        simulation,
        float_1,
        float_2,
        float_3,
        float_4,
        float_5,
        float_6,
        float_7,
        float_8,

        # float_9,
        # float_10,
        # float_11,
        # float_12,
        # float_13,
        vis,
    ])    