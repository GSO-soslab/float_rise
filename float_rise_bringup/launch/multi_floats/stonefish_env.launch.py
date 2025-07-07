import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription, LaunchContext
from launch.actions import (
    IncludeLaunchDescription,
    DeclareLaunchArgument,
    OpaqueFunction,
    TimerAction
)
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration

def generate_robot_launches(context: LaunchContext):
    """
    This function is executed at launch time and generates the IncludeLaunchDescription
    actions for each robot, with a configurable delay between each launch.
    """
    # Get the number of robots from its launch argument
    num_robots_str = context.perform_substitution(LaunchConfiguration('num_robots'))
    
    # Get the launch delay from its launch argument
    launch_delay_str = context.perform_substitution(LaunchConfiguration('launch_delay'))

    # Perform type conversion with error handling
    try:
        num_robots = int(num_robots_str)
        launch_delay = float(launch_delay_str)
    except ValueError as e:
        raise RuntimeError(f"Could not convert launch argument to a number: {e}")

    print(f"--- Generating {num_robots} robot launches with a {launch_delay}s delay between each ---")

    robot_bringup_pkg = 'float_rise_bringup'
    robot_launch_file_path = os.path.join(
        get_package_share_directory(robot_bringup_pkg),
        'launch',
        'multi_floats',
        'stonefish_float.launch.py'
    )

    launch_actions = []
    for i in range(num_robots):
        robot_id = i + 1
        
        robot_launch_action = IncludeLaunchDescription(
            PythonLaunchDescriptionSource(robot_launch_file_path),
            launch_arguments={
                'arg_robot_id': str(robot_id),
                'arg_robot_name': 'float_rise',
            }.items()
        )
        
        # Calculate delay using the value from the launch argument
        delay = i * launch_delay

        delayed_launch = TimerAction(
            period=delay,
            actions=[robot_launch_action]
        )
        launch_actions.append(delayed_launch)

    return launch_actions


def generate_launch_description():
    
    # ======================================================================= #
    # simulator setup
    # ======================================================================= #
    world_of_stonefish_dir = get_package_share_directory('world_of_stonefish')
    sim_world = 'multiple_floats.scn'
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
        arguments=[
            simulation_data, scenario_desc, simulation_rate, 
            window_res_x, window_res_y, rendering_quality]
    )
    
    # ======================================================================= #
    # launch arguments
    # ======================================================================= #
    
    declare_num_robots_arg = DeclareLaunchArgument(
        'num_robots',
        default_value='2',
        description='The number of float robots to launch.'
    )

    declare_launch_delay_arg = DeclareLaunchArgument(
        'launch_delay',
        default_value='0.0',
        description='Delay in seconds between launching each robot stonefish convertor'
    )

    generate_robots_action = OpaqueFunction(function=generate_robot_launches)

    # ======================================================================= #
    # all the nodes
    # ======================================================================= #
    return LaunchDescription([
        declare_num_robots_arg,

        declare_launch_delay_arg,

        stonefish,

        generate_robots_action,
    ])