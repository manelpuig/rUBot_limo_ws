# **2. LIMO Bringup**

This repository is used for LIMO robot simulation in ROS Noetic

References:

- bitbucket: https://bitbucket.org/theconstructcore/limo_robot/src/main/


## **2.1. Bringup and control in Virtual environment**

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

## **2.2. Bringup and control of real Limo robot**

To bringup HW:

### **a) Bringup only base**

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


### **b) Bringup with LiDAR**

````shell
cd /home/agilex/agilex_ws
roslaunch limo_bringup limo_start.launch pub_odom_tf:=false
roslaunch limo_bringup lidar_rviz.launch
````
