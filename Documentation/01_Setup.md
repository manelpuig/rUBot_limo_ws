# **1. Setup**

This repository is used for LIMO robot simulation in ROS Noetic

References:
- https://github.com/limo-agx
- https://github.com/limo-agx/limo
- https://github.com/limo-agx/limo_desktop
- https://github.com/limo-agx/limo_simulator
- https://limo-agx.github.io
- https://bitbucket.org/theconstructcore/limo_robot/src/main/



## **Instructions**

- Create a local "project rUBot_limo_ws" with VS code
- Create a "src" folder
- Clone inside the repositories:
````shell
cd src
git clone https://github.com/limo-agx/limo.git
git clone https://github.com/limo-agx/limo_desktop.git
git clone https://github.com/limo-agx/limo_simulator.git
````
- delete the .git folders in the cloned packages
- Create and sync a new repository in github within VS code in "source control" option

Once the github repository is created you can open the ROS environment (i.e. TheConstruct environment)
- clone the "rUBot_limo_ws" repository on Home ROS environment:
````shell
git clone https://github.com/manelpuig/rUBot_limo_ws.git
````
- install dependencies and build
````shell
cd ..
rosdep install --from-paths src --ignore-src -y
catkin_make
source devel/setup.bash
````
## **Bringup and control**

To bringup the Limo robot in simulation environment:
- The Differential Drive model
````shell
roslaunch limo_gazebo limo_four_diff.launch 
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