from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch.substitutions import PythonExpression
from launch.actions import TimerAction
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os
import yaml

def generate_launch_description():

    ###########################################################################
    ## Node Arguments
    ###########################################################################      
    robot_name = LaunchConfiguration('robot_name')
    mission_delay = LaunchConfiguration('mission_delay')

    ###########################################################################
    ## mvp_mission param
    ###########################################################################    
    mission_param_file = os.path.join(
        get_package_share_directory('float_rise_bringup'),
        'config',
        'float',
        'mvp_mission.yaml'
    )

    ###########################################################################
    ## behaviors param
    ###########################################################################    
    bhv_param_file = os.path.join(
        get_package_share_directory('float_rise_bringup'),
        'config',
        'float',
        'bhv_params.yaml'
    )

    with open(bhv_param_file, 'r') as f:
        bhv_params = yaml.safe_load(f)
    # Add prefix to parameter names
    bhv_prefixed_params = {}
    # Process each section in the YAML file
    for bhv_name, bhv_params in bhv_params.items():
        # Use section name as prefix
        bhv_prefix = bhv_name + '/'  
        bhv_prefixed_params.update({
            bhv_prefix + key: value for key, value in bhv_params.items()})

    ###########################################################################
    ## helm param 
    ###########################################################################

    mvp_helm_config_file = os.path.join(
        get_package_share_directory('float_rise_config'),
        'mvp_mission_config',
        'float',
        'helm.yaml'
    )

    ###########################################################################
    ## The Node 
    ###########################################################################
    
    node = Node(
        package="mvp_helm",
        executable="mvp_helm",
        namespace=robot_name,
        name="mvp_helm",
        prefix=['stdbuf -o L'],
        output="screen",
        remappings=[
            ('datum', 'gps/datum'),
        ],
        parameters=[
            {'helm_config_file': mvp_helm_config_file},
            {'tf_prefix': robot_name},
            mission_param_file,
            bhv_prefixed_params
        ],
        emulate_tty=True        
    )
        
    return LaunchDescription([

        # Decalre arguments
        DeclareLaunchArgument(
            'robot_name', default_value = 'my_robot'            
        ),

        DeclareLaunchArgument(
            'mission_delay', default_value = '0.0'            
        ),

        # Delay the node if needed
        TimerAction(
            period=PythonExpression([mission_delay]),
            actions=[node]
        ),
    ])
