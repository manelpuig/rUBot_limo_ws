# **1. LIMO robot Setup**

This repository is used for LIMO robot simulation in ROS Noetic

References:

- Web Manual: https://docs.trossenrobotics.com/agilex_limo_docs/
- Manual (pdf): https://static.generation-robots.com/media/limo-standard-user-manual-en.pdf
- Manual (Web): https://github.com/agilexrobotics/limo-doc/blob/master/Limo%20user%20manual(EN).md
- github: https://github.com/agilexrobotics/limo_ros/tree/master
- RTABMAP: https://docs.trossenrobotics.com/agilex_limo_docs/demos/slam_nav/rtabmap.html
- Doc_tutorial: https://limo-agx.github.io
- Github: https://github.com/limo-agx
- Github: https://github.com/limo-agx/limo
- Github: https://github.com/limo-agx/limo_desktop
- Github: https://github.com/limo-agx/limo_simulator
- bitbucket: https://bitbucket.org/theconstructcore/limo_robot/src/main/

## **1.1. Simulation LIMO robot**

We have created a "rUBot_limo_ws" github repository to fork on your github account and clone to your ROS environment (i.e. TheConstruct environment)

To create this repository we have followed the Agilex instructions:
````shell
mkdir -p ~/rUBot_limo_ws/src
cd ~/rUBot_limo_ws/src
# download source code
git clone https://github.com/limo-agx/limo.git
git clone https://github.com/limo-agx/limo_desktop.git
git clone https://github.com/limo-agx/limo_simulator.git
git clone https://github.com/limo-agx/limo_vision.git
git clone https://github.com/limo-agx/limo_robot.git
cd ~/rUBot_limo_ws
catkin_make
````
This is already done and ready to work:

- clone the "rUBot_limo_ws" repository on Home ROS environment:
````shell
git clone https://github.com/manelpuig/rUBot_limo_ws.git
````
- install dependencies and build
````shell
cd ..
catkin_make
source devel/setup.bash
````
- Add in .bashrc the lines:
````shell
source /opt/ros/noetic/setup.bash
source /home/user/rUBot_limo_ws/devel/setup.bash
cd /home/user/rUBot_limo_ws
````
## **1.2. Real LIMO robot**

Documentation:
- https://github.com/agilexrobotics/limo_ros
- https://github.com/agilexrobotics/limo-doc/blob/master/Limo%20user%20manual(EN).md
- https://github.com/agilexrobotics/limo_ros2/tree/humble
- https://github.com/agilexrobotics/limo_pro_doc/blob/master/Limo%20Pro%20Ros2%20Foxy%20user%20manual(EN).md

### **1.2.1. Setup on Ubuntu Desktop**

We can take the created repositories in limo robot (for ROs Noetic and RO2 Foxy):
- ROS Noetic:
````shell
cd /home/agilex/agilex_ws
````
- ROS2 Foxy
````shell
cd /home/agilex/agilex_ws
````
You can simply source the .bashrc and work inside the repository.

### **1.2.1. Setup on Docker**

The available repositories in real LIMO robot Jetson Nano computer onboard are on ROS1 Noetic and ROS2 Foxy. If you want to work on other ROS distributions the best method is to use Docker images:
- The process is describerd for ROS1 Noetic in: https://bitbucket.org/theconstructcore/agilex_limo/src/master/
- The process is describerd for ROS2 Humble in: https://hub.docker.com/r/theconstructai/limo

