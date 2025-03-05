
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

        # connect the float1 and float2
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='float1_float2',
            arguments = ["0.0", "0.0", "0.0", "0.0", "0.0", "0.0", 'float_rise_1/world', 'float_rise_2/world']    
        ),

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
