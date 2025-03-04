# Floats simulation for the [RISE project](https://soslab.wordpress.com/rise/)

## Introduction
This is a repository of the simulation for swarm floats with acoustic devices (e.g., USBL or Acoustic modem).
- Tested environment
    - ROS version: Jazzy
    - Ubuntu: 24.04
- Directory information
    - `float_rise_bringup` 
        - `launch` includes launch files
            - `bringup_simulation_1.launch.py` is the main launch file to bring up the simulation environment
            - `include` folder include all files called in the main bringup simulation file.
        - `config` includes all ros params *.yaml files which are called in the sub launch file in the `include` folder.
    - `float_rise_config` include MVP configuration files. The files are in yaml format and was loaded in mvp code using yaml-cpp.

    - `float_rise_description` include urdf files and rviz configuration files.

## Simulation Related Installation

### Stonefish Simulator
We use [Stonefish](https://github.com/patrykcieslak/stonefish) Simulator for our system development.
Our configuration is tested with our forked Stonefish, which may sometimes lack behind the original repository. We will make sure we are up-to-date with the [original repository](https://github.com/patrykcieslak/stonefish).
#### Installatin
- Download the stonefish repository
    ```shell
    cd ~/YOUR_DEV_WORKSPACE
    git clone https://github.com/patrykcieslak/stonefish.git
    ```
- Download dependencies: `sudo apt update && sudo apt install libglm-dev libsdl2-dev libfreetype6-dev`

- Fix a file in SDL2 library
    - `cd /usr/lib/x86_64-linux-gnu/cmake/SDL2/`
    - `sudo nano sdl2-config.cmake`
    - Remove space after "-lSDL2".
    - Save the file.

- Build the stonefish
```sh
cd ~YOUR_DEV_WORKSPACE/stonefish
mkdir build
cd build
cmake ..
make -j$(nproc)
sudo make install
```

- For more information about stonefish please check the original [repository](https://github.com/patrykcieslak/stonefish) and the [documentation](https://stonefish.readthedocs.io/en/latest/).

- you may need pcl library: `sudo apt install libpcl-dev`

- you may encounter build error in regarding `Sample.h` file. If so add `#include <cstdint>` in `/stonefish/Library/include/sensors/Sample.h` will solve the problem.    


## ROS2 simulation packages

### Stonefish ROS2 wrapper
Our code is tested with the forked Stonefish ROS2 wrapper. We will make sure we are up-to-date with the original Stonefish ROS2 wrapper.
The original wrapper can be found [here](https://github.com/patrykcieslak/stonefish_ros2)
- Download the forked ROS2 wrapper 
```sh
cd ~/YOUR_ROS2_WORKSPACE/src
git clone https://github.com/GSO-soslab/stonefish_ros2
cd stonefish_ros2
git checkout jazzy-devel
```

### World of stonefish
All the simulator files related to stonefish simulator are included in the `world_of_stonefish` repository. Sepcfically, the repository has stonefish scenario files and drivers that connects stonefish sensor messages into MVP compatible messages.

- Download the repository
```sh
cd ~/YOUR_ROS2_WORKSPACE/src
git clone https://github.com/GSO-soslab/world_of_stonefish.git
cd world_of_stonefish
git checkout jazzy-devel-floats
```

## ROS2 MVP frameworks
MVP frame work is our Guidance Navigation and Control framework.
   
### Robot localization
The localization part uses the `robot_localization` package that is available [here](https://github.com/cra-ros-pkg/robot_localization.git)
- Installation
```sh
sudo apt install ros-jazzy-robot-localization
```

### MVP utilies
This package contains utilites scripts for localization and topic conversions.
- installation
```sh
cd ~/YOUR_ROS2_WORKSPACE/src
git clone https://github.com/uri-ocean-robotics/mvp_utilities.git
cd mvp_utilities
git checkout jazzy-devel
```

### MVP control
MVP control is the low-level controller we developed. It accepts desired pose and outputs thruster commands to control the vehice pose in a specific frame.
- Installation
```sh
cd ~/YOUR_ROS2_WORKSPACE/src
git clone https://github.com/uri-ocean-robotics/mvp_control.git
cd mvp_control
git checkout jazzy-devel
```      

- Install gsl library: `sudo apt-get install libgsl-dev`
    

### MVP mission
This is the high level guidance system.
We are currently migrating our ROS1 mvp_mission into ROS2 version.
- Installation
```sh
cd ~/YOUR_ROS2_WORKSPACE/src
git clone https://github.com/uri-ocean-robotics/mvp_mission.git
cd mvp_mission
git checkout jazzy-devel
```    

### MVP Message
Our MVP frame uses the MVP messages which has customized ROS message and services for the MVP framework.
- Installation
```sh
cd ~/YOUR_ROS2_WORKSPACE/src
git clone https://github.com/uri-ocean-robotics/mvp_msgs.git
cd mvp_msgs
git checkout jazzy-devel
```   

### Acomm Message
Our MVP frame uses the acomms messgae to handle USBL and Acoustic Modem data transmission.
- Installation
```sh
cd ~/YOUR_ROS2_WORKSPACE/src
git https://github.com/GSO-soslab/acomms_msgs
cd acomms_msgs
git checkout jazzy-devel
```           

## Building the workspace
After all the software are downloaded or installed from the previous section you can compile your ROS2 workspace.
```sh
cd ~/Your_ROS2_WORKSPACE
colcon build --parallel-worker $(nproc)
```

## Testing the robot with Stonefish
- Launch the simulator
```sh
cd ~/Your_ROS2_WORKSPACE
source install/setup.bash && ros2 launch float_rise_bringup bringup_simulation_1.launch.py
```
- Enable the controller: 
    - inside `rqt`, find srv: `/float_rise/controller/set`, 
    - set the Expression of `data` to `True`

- Start a mission:
    - insde `rqt`, find srv: `/float_rise/mvp_helm/change_state`
    - set the Expression of `state` to `floating`
    - set the Expression of `caller` to `rqt`
