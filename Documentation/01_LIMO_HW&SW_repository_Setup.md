# **1. LIMO HW&SW repository Setup**

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

## **Repository Setup Instructions**

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

## **Bringup and control in Virtual environment**

To bringup the Limo robot in simulation environment:
- The Differential Drive model
````shell
roslaunch limo_gazebo limo_four_diff.launch 
````
- The Mecanum Drive model
````shell
roslaunch limo_gazebo limo_mecanum.launch 
````
- The Ackerman Drive model:
````shell
roslaunch limo_gazebo limo_ackerman.launch 
````
To view the robot in RVIZ:
````shell
roslaunch limo_viz view_four_diff_model.launch
````
To control using keyboard:
````shell
rosrun teleop_twist_keyboard teleop_twist_keyboard.py
````
or The terminal:
````shell
rostopic pub -r 1 /cmd_vel geometry_msgs/Twist '[1, 0, 0]' '[0, 0, 1]'
````

## **Bringup and control of real Limo robot**

To bringup HW:

### **1. Bringup only base**

````shell
cd /home/agilex/agilex_ws
roslaunch limo_base limo_base.launch
roslaunch limo_bringup limo_teletop_keyboard.launch
````

Control on python:
````shell
cd /home/agilex/agilex_ws/src/limo_ros/limo_base/script
python3 limomove.py
````
We have to install pylimo


### **2. Bringup with LiDAR**

````shell
cd /home/agilex/agilex_ws
roslaunch limo_bringup limo_start.launch pub_odom_tf:=false
roslaunch limo_bringup lidar_rviz.launch
````
