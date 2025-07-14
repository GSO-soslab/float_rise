
from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node
import os

def generate_launch_description():

    rviz_config_dir = os.path.join( 
        get_package_share_directory('float_rise_description'), 'config', 'rviz.rviz' )
    rqt_config_dir = os.path.join( 
        get_package_share_directory('float_rise_description'), 'config', 'rqt.perspective' )

    return LaunchDescription([

        # =================================================================== #
        # TF for float_1 and any other float_# for world
        # so you can get noise tf between each float
        # =================================================================== #

        # connect the float1 and float2
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='float1_float2',
            arguments = ["0.0", "0.0", "0.0", "0.0", "0.0", "0.0", 'float_rise_1/world', 'float_rise_2/world']    
        ),

        # connect the float1 and float3
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='float1_float3',
            arguments = ["0.0", "0.0", "0.0", "0.0", "0.0", "0.0", 'float_rise_1/world', 'float_rise_3/world']    
        ),

        # connect the float1 and float4
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='float1_float4',
            arguments = ["0.0", "0.0", "0.0", "0.0", "0.0", "0.0", 'float_rise_1/world', 'float_rise_4/world']    
        ),

        # connect the float1 and float5
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='float1_float5',
            arguments = ["0.0", "0.0", "0.0", "0.0", "0.0", "0.0", 'float_rise_1/world', 'float_rise_5/world']    
        ),

        # connect the float1 and float6
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='float1_float6',
            arguments = ["0.0", "0.0", "0.0", "0.0", "0.0", "0.0", 'float_rise_1/world', 'float_rise_6/world']    
        ),

        # connect the float1 and float7
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='float1_float7',
            arguments = ["0.0", "0.0", "0.0", "0.0", "0.0", "0.0", 'float_rise_1/world', 'float_rise_7/world']    
        ),

        # connect the float1 and float8
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='float1_float8',
            arguments = ["0.0", "0.0", "0.0", "0.0", "0.0", "0.0", 'float_rise_1/world', 'float_rise_8/world']    
        ),

        # connect the float1 and float9
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='float1_float9',
            arguments = ["0.0", "0.0", "0.0", "0.0", "0.0", "0.0", 'float_rise_1/world', 'float_rise_9/world']    
        ),        

        # =================================================================== #
        # TF for world_ned and world for each float
        # =================================================================== #

        # connect world and world_ned for float1
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='float1_world_ned',
            arguments = ["0.0", "0.0", "0.0", "1.571", "0.0", "3.1415", 'float_rise_1/world', 'float_rise_1/world_ned']    
        ),

        # connect world and world_ned for float2
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='float2_world_ned',
            arguments = ["0.0", "0.0", "0.0", "1.571", "0.0", "3.1415", 'float_rise_2/world', 'float_rise_2/world_ned']    
        ),        

        # connect world and world_ned for float3
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='float3_world_ned',
            arguments = ["0.0", "0.0", "0.0", "1.571", "0.0", "3.1415", 'float_rise_3/world', 'float_rise_3/world_ned']    
        ),    

        # connect world and world_ned for float4
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='float4_world_ned',
            arguments = ["0.0", "0.0", "0.0", "1.571", "0.0", "3.1415", 'float_rise_4/world', 'float_rise_4/world_ned']    
        ),    

        # connect world and world_ned for float5
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='float5_world_ned',
            arguments = ["0.0", "0.0", "0.0", "1.571", "0.0", "3.1415", 'float_rise_5/world', 'float_rise_5/world_ned']    
        ),    

        # connect world and world_ned for float6
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='float6_world_ned',
            arguments = ["0.0", "0.0", "0.0", "1.571", "0.0", "3.1415", 'float_rise_6/world', 'float_rise_6/world_ned']    
        ),    

        # connect world and world_ned for float7
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='float7_world_ned',
            arguments = ["0.0", "0.0", "0.0", "1.571", "0.0", "3.1415", 'float_rise_7/world', 'float_rise_7/world_ned']    
        ),    

        # connect world and world_ned for float8
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='float8_world_ned',
            arguments = ["0.0", "0.0", "0.0", "1.571", "0.0", "3.1415", 'float_rise_8/world', 'float_rise_8/world_ned']    
        ),  

        # connect world and world_ned for float9
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='float9_world_ned',
            arguments = ["0.0", "0.0", "0.0", "1.571", "0.0", "3.1415", 'float_rise_9/world', 'float_rise_9/world_ned']    
        ),  

        # rviz
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            arguments=['-d', [rviz_config_dir]],
        ),

        # rqt
        Node(package="rqt_gui", 
             executable="rqt_gui", 
             name="rqt", 
             arguments=["--perspective-file", rqt_config_dir],
        ),
])
