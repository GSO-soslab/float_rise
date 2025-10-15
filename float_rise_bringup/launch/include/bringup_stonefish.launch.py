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
    # sim_world = 'swarm_floats.scn'
    sim_world = 'multiple_floats.scn'
    simulation_data = os.path.join(world_of_stonefish_dir, 'data/')
    scenario_desc = os.path.join(world_of_stonefish_dir, 'world', sim_world)
    simulation_rate = "100"
    window_res_x = "1000"
    window_res_y = "1000"
    rendering_quality ="low"

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
    # bringup simulated vehicles
    # ======================================================================= #
    robot_bringup = 'float_rise_bringup'

    # bringup the float-1
    sim_float_1 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory(robot_bringup),
            'launch', 'include', 'float_1', 'float_1.launch.py')]),
        launch_arguments = {
            'arg_robot_name': 'float_rise_1',
            'arg_world_frame': 'float_rise_1/world',
            'arg_imu_frame': 'float_rise_1/imu_sf'
        }.items()    
    )   

    # bringup the float-2
    sim_float_2 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory(robot_bringup),
            'launch', 'include', 'float_2', 'float_2.launch.py')]),
        launch_arguments = {
            'arg_robot_name': 'float_rise_2',
            'arg_world_frame': 'float_rise_2/world',
            'arg_imu_frame': 'float_rise_2/imu_sf'
        }.items()    
    )  

    # bringup the float-3
    sim_float_3 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory(robot_bringup),
            'launch', 'include', 'float_3', 'float_3.launch.py')]),
        launch_arguments = {
            'arg_robot_name': 'float_rise_3',
            'arg_world_frame': 'float_rise_3/world',
            'arg_imu_frame': 'float_rise_3/imu_sf'
        }.items()    
    )      

    # # bringup the float-4
    # sim_float_4 = IncludeLaunchDescription(
    #     PythonLaunchDescriptionSource([
    #         os.path.join(get_package_share_directory(robot_bringup),
    #         'launch', 'include', 'float_4', 'float_4.launch.py')]),
    #     launch_arguments = {
    #         'arg_robot_name': 'float_rise_4',
    #         'arg_world_frame': 'float_rise_4/world',
    #         'arg_imu_frame': 'float_rise_4/imu_sf'
    #     }.items()    
    # )  

    # # bringup the float-5
    # sim_float_5 = IncludeLaunchDescription(
    #     PythonLaunchDescriptionSource([
    #         os.path.join(get_package_share_directory(robot_bringup),
    #         'launch', 'include', 'float_5', 'float_5.launch.py')]),
    #     launch_arguments = {
    #         'arg_robot_name': 'float_rise_5',
    #         'arg_world_frame': 'float_rise_5/world',
    #         'arg_imu_frame': 'float_rise_5/imu_sf'
    #     }.items()    
    # ) 
    
    # # bringup the float-6
    # sim_float_6 = IncludeLaunchDescription(
    #     PythonLaunchDescriptionSource([
    #         os.path.join(get_package_share_directory(robot_bringup),
    #         'launch', 'include', 'float_6', 'float_6.launch.py')]),
    #     launch_arguments = {
    #         'arg_robot_name': 'float_rise_6',
    #         'arg_world_frame': 'float_rise_6/world',
    #         'arg_imu_frame': 'float_rise_6/imu_sf'
    #     }.items()    
    # )   

    # # bringup the float-7
    # sim_float_7 = IncludeLaunchDescription(
    #     PythonLaunchDescriptionSource([
    #         os.path.join(get_package_share_directory(robot_bringup),
    #         'launch', 'include', 'float_7', 'float_7.launch.py')]),
    #     launch_arguments = {
    #         'arg_robot_name': 'float_rise_7',
    #         'arg_world_frame': 'float_rise_7/world',
    #         'arg_imu_frame': 'float_rise_7/imu_sf'
    #     }.items()    
    # )   

    # # bringup the float-8
    # sim_float_8 = IncludeLaunchDescription(
    #     PythonLaunchDescriptionSource([
    #         os.path.join(get_package_share_directory(robot_bringup),
    #         'launch', 'include', 'float_8', 'float_8.launch.py')]),
    #     launch_arguments = {
    #         'arg_robot_name': 'float_rise_8',
    #         'arg_world_frame': 'float_rise_8/world',
    #         'arg_imu_frame': 'float_rise_8/imu_sf'
    #     }.items()    
    # )  

    # # bringup the float-9
    # sim_float_9 = IncludeLaunchDescription(
    #     PythonLaunchDescriptionSource([
    #         os.path.join(get_package_share_directory(robot_bringup),
    #         'launch', 'include', 'float_9', 'float_9.launch.py')]),
    #     launch_arguments = {
    #         'arg_robot_name': 'float_rise_9',
    #         'arg_world_frame': 'float_rise_9/world',
    #         'arg_imu_frame': 'float_rise_9/imu_sf'
    #     }.items()    
    # )  

    # # bringup the float-10
    # sim_float_10 = IncludeLaunchDescription(
    #     PythonLaunchDescriptionSource([
    #         os.path.join(get_package_share_directory(robot_bringup),
    #         'launch', 'include', 'float_10', 'float_10.launch.py')]),
    #     launch_arguments = {
    #         'arg_robot_name': 'float_rise_10',
    #         'arg_world_frame': 'float_rise_10/world',
    #         'arg_imu_frame': 'float_rise_10/imu_sf'
    #     }.items()    
    # )  

    # # bringup the float-11
    # sim_float_11 = IncludeLaunchDescription(
    #     PythonLaunchDescriptionSource([
    #         os.path.join(get_package_share_directory(robot_bringup),
    #         'launch', 'include', 'float_11', 'float_11.launch.py')]),
    #     launch_arguments = {
    #         'arg_robot_name': 'float_rise_11',
    #         'arg_world_frame': 'float_rise_11/world',
    #         'arg_imu_frame': 'float_rise_11/imu_sf'
    #     }.items()    
    # )

    # # bringup the float-12
    # sim_float_12 = IncludeLaunchDescription(
    #     PythonLaunchDescriptionSource([
    #         os.path.join(get_package_share_directory(robot_bringup),
    #         'launch', 'include', 'float_12', 'float_12.launch.py')]),
    #     launch_arguments = {
    #         'arg_robot_name': 'float_rise_12',
    #         'arg_world_frame': 'float_rise_12/world',
    #         'arg_imu_frame': 'float_rise_12/imu_sf'
    #     }.items()    
    # )

    # # bringup the float-13
    # sim_float_13 = IncludeLaunchDescription(
    #     PythonLaunchDescriptionSource([
    #         os.path.join(get_package_share_directory(robot_bringup),
    #         'launch', 'include', 'float_13', 'float_13.launch.py')]),
    #     launch_arguments = {
    #         'arg_robot_name': 'float_rise_13',
    #         'arg_world_frame': 'float_rise_13/world',
    #         'arg_imu_frame': 'float_rise_13/imu_sf'
    #     }.items()    
    # )

    # ======================================================================= #
    # all the nodes
    # ======================================================================= #
    return LaunchDescription([
        stonefish,
        sim_float_1,
        sim_float_2,
        sim_float_3,
        # sim_float_4,
        # sim_float_5,
        # sim_float_6,
        # sim_float_7,
        # sim_float_8,

        # sim_float_9,
        # sim_float_10,
        # sim_float_11,
        # sim_float_12,
        # sim_float_13,
    ])