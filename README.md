# Floats simulation for the [RISE project](https://soslab.wordpress.com/rise/)

## Introduction
This is a repository of the simulation for swarm floats with acoustic devices (e.g., USBL or Acoustic modem).
- Tested environment
    - ROS version: Jazzy
    - Ubuntu: 24.04
- Directory information
    - `float_rise` empty folder
    - `float_rise_bringup` 
        - `launch` includes launch files
            - `include` folder include all files called in the main bringup simulation file.
        - `config` includes all ros params *.yaml files which are called in the sub launch file in the `include` folder.
    - `float_rise_config` include MVP configuration files. The files are in yaml format and was loaded in mvp code using yaml-cpp.
    - `float_rise_description` include urdf files and rviz configuration files.

## Simulation Related Installation

### Stonefish Simulator
We use [Stonefish](https://github.com/patrykcieslak/stonefish) Simulator for our system development.
#### Installatin
- Download the stonefish repository
    ```shell
    cd ~/YOUR_DEV_WORKSPACE
    git clone --branch jazzy-devel-floats https://github.com/GSO-soslab/stonefish
    ```
- Download dependencies: `sudo apt update && sudo apt install libglm-dev libsdl2-dev libfreetype6-dev libpcl-dev`

<!-- - Fix a file in SDL2 library
    - `cd /usr/lib/x86_64-linux-gnu/cmake/SDL2/`
    - `sudo nano sdl2-config.cmake`
    - Remove space after "-lSDL2".
    - Save the file. -->

- Build the stonefish
```sh
cd ~/YOUR_DEV_WORKSPACE/stonefish
mkdir build
cd build
cmake ..
make -j$(nproc)
sudo make install
```

- For more information about stonefish please check the original [repository](https://github.com/patrykcieslak/stonefish) and the [documentation](https://stonefish.readthedocs.io/en/latest/).


## ROS2 related

```sh
# some packages:
sudo apt install ros-jazzy-robot-localization libgsl-dev

# Acomm Messages:
#   The ROS2 message type to handle USBL and Acoustic Modem data transmission.
cd ~/YOUR_ROS2_WORKSPACE/src
git clone --branch jazzy-devel https://github.com/GSO-soslab/acomms_msgs
cd acomms_msgs
git checkout -b d46c726
cd ..

# Float Planner:
#   This package handle the multiple floats running the up-down motions
git clone --branch main https://github.com/GSO-soslab/float_planner

# Float RISE:
#   This package contain all the files to launch the multi-floats simulation
git clone --branch jazzy-devel https://github.com/GSO-soslab/float_rise

#  MVP Control:
#   This is the low-level controller for the vehicle. It accepts desired pose and outputs thruster commands to control the vehice pose in a specific frame.
git clone --branch jazzy-devel https://github.com/uri-ocean-robotics/mvp_control
cd mvp_control
git checkout -b 76f6dd8
cd ..

# MVP Mission:
#   This is the the high level guidance system 
git clone --branch jazzy-devel https://github.com/uri-ocean-robotics/mvp_mission
cd mvp_mission
git checkout -b 841cde7
cd ..

# MVP MSG:
#   This is the package contains custom defined ROS2 messages
git clone --branch jazzy-devel https://github.com/uri-ocean-robotics/mvp_msgs
cd mvp_msgs
git checkout -b 64b119c
cd ..

# MVP Utilites:
#   This package contains utilites scripts for localization and topic conversions
git clone --branch jazzy-devel https://github.com/uri-ocean-robotics/mvp_utilities
cd mvp_utilities
git checkout -b e0a62ea
cd ..

# Stonefish ROS2 wrapper:
#   This wrapper is publish all the simulated sesnor data into ros2 msg.
git clone --branch jazzy-devel https://github.com/GSO-soslab/stonefish_ros2
cd stonefish_ros2
git checkout -b c534077
cd ..

# Stonefish setup:
#    All the simulator files related to stonefish simulator are included in this package.
git clone --branch jazzy-devel-floats https://github.com/GSO-soslab/world_of_stonefish

# RNN velocity prediction (optional)
#   This package will estimate the float 3-axis velocity based on given input(IMU data, voltage(assume 0 here), ...)
git clone --branch jazzy-devel-float https://github.com/GSO-soslab/ros_velocity_prediction

```         

## Building the workspace
After all the software are downloaded or installed from the previous section you can compile your ROS2 workspace.
```sh
cd ~/Your_ROS2_WORKSPACE
colcon build --parallel-worker $(nproc)
```

## Testing the robot with Stonefish
- Launch the simulator in termianl 1
```sh
cd ~/Your_ROS2_WORKSPACE
source install/setup.bash 
ros2 launch float_rise_bringup bringup_simulation_13_floats.launch.py
```

- Launch multi-float motions in temrianl 2
```sh
cd ~/Your_ROS2_WORKSPACE
source install/setup.bash 
ros2 launch float_planner float_planner.launch.py
```