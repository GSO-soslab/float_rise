import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    

    # ======================================================================= #
    # simulator setup
    # ======================================================================= #
    world_of_stonefish_dir = get_package_share_directory('world_of_stonefish')
    sim_world = 'swarm_floats.scn'
    simulation_data = os.path.join(world_of_stonefish_dir, 'data/')
    scenario_desc = os.path.join(world_of_stonefish_dir, 'world', sim_world)
    simulation_rate = "100"
    window_res_x = "800"
    window_res_y = "800"
    rendering_quality ="high"

    stonefish = Node(
        package="stonefish_ros2",
        executable="stonefish_simulator",
        name="stonefish_simulator",
        # output="screen",
        arguments=[
            simulation_data, scenario_desc, simulation_rate, 
            window_res_x, window_res_y, rendering_quality]
    )
    
    # ======================================================================= #
    # floats
    # ======================================================================= #
    robot_bringup = 'float_rise_bringup'

    # bringup the first float
    float_1 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory(robot_bringup),
            'launch', 'include', 'stonefish_float.launch.py')]),
        launch_arguments = {
            'arg_robot_name': 'float_rise_1',
            'arg_world_frame': 'float_rise_1/world',
            'arg_imu_frame': 'float_rise_1/imu_sf'
        }.items()    
    )   

    # bringup the second float
    float_2 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory(robot_bringup),
            'launch', 'include', 'stonefish_float.launch.py')]),
        launch_arguments = {
            'arg_robot_name': 'float_rise_2',
            'arg_world_frame': 'float_rise_2/world',
            'arg_imu_frame': 'float_rise_2/imu_sf'
        }.items()    
    )  

    # ======================================================================= #
    # all the nodes
    # ======================================================================= #
    return LaunchDescription([
        stonefish,
        float_1,
        float_2,
    ])