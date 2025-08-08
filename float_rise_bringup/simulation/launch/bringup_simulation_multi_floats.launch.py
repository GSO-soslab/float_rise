import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, PythonExpression
import time


def generate_launch_description():
    robot_num = 2

    # =================================================== #
    # bringup everything related to stonefish simulator
    # =================================================== #

    simulation = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory('float_rise_bringup'), 
            'launch', 'multi_floats', 'bringup_stonefish.launch.py')]),
        launch_arguments = {
            'num_robots' : str(robot_num),
        }.items()   
    )    

    # =================================================== #
    # bringup everything related to ros setup for float 1
    # =================================================== #

    ### TODO: all the node has same namespace: such as 3 float_rise_1/mvp_helm
    # floats = IncludeLaunchDescription(
    #     PythonLaunchDescriptionSource([
    #         os.path.join(get_package_share_directory('float_rise_bringup'), 
    #         'launch', 'multi_floats', 'bringup_multi_nav.launch.py')]),
    #     launch_arguments = {
    #         'num_robots' : str(robot_num),
    #         'launch_delay' : '1.0',
    #     }.items()   
    # )    

    ### TODO: control_delay not exits...
    # floats = IncludeLaunchDescription(
    #     PythonLaunchDescriptionSource([
    #         os.path.join(get_package_share_directory('float_rise_bringup'), 
    #         'launch', 'multi_floats', 'bringup_nav_stack.launch.py')]),
    #     launch_arguments = {
    #         'num_robots' : str(robot_num),
    #         'launch_delay' : '5.0',
    #     }.items()   
    # )    

    float_1 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory('float_rise_bringup'), 
            'launch', 'multi_floats', 'bringup_navigation.launch.py')]),
        launch_arguments = {
            'robot_name' : 'float_rise_1',
        }.items()   
    )   

    # float_2 = IncludeLaunchDescription(
    #     PythonLaunchDescriptionSource([
    #         os.path.join(get_package_share_directory('float_rise_bringup'), 
    #         'launch', 'multi_floats', 'bringup_navigation.launch.py')]),
    #     launch_arguments = {
    #         'robot_name' : 'float_rise_2',
    #     }.items()   
    # )   

    # =================================================== #
    # bringup visualization
    # =================================================== #

    vis = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory('float_rise_bringup'), 
            'launch', 'multi_floats', 'bringup_visualization.launch.py')]),
        # launch_arguments = {'arg_robot_name': arg_robot_name}.items()    
    )    

    return LaunchDescription([
        simulation,
        # floats,
        float_1,
        # float_2,
        # float_3,
        vis,
    ])    