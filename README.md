# Computer Vision Tutorial

- The publisher/subscriber and OpenCV portion is based on this [ROS tutorial](http://wiki.ros.org/cv_bridge/Tutorials/ConvertingBetweenROSImagesAndOpenCVImagesPython)

## Prerequisites
- Install Ubuntu in Virtual Machine or Dual boot (Ubuntu 20 preferred)
- Install ROS (ROS Noetic preferred)

## Cloning the repo
Go to home directory if you're not already there
```
cd ~
```
Run following commands
```
mkdir -p catkin_ws/src
cd catkin_ws/src
git clone https://github.com/utra-robosoccer/Computer-Vision-Tutorial.git
```

## Updating Dependencies
The following commands will look inside package.xml and install opencv for you
```
cd ~/catkin_ws/
rosdep update
rosdep install --from-paths src --ignore-src -r -y --rosdistro noetic
```

## Building tutorial package
Sourcing setup file lets your computer know where your project files are
```
cd ~/catkin_ws
catkin build computer_vision_pkg
source devel/setup.bash
```


## Launch the robot
```
roslaunch computer_vision_pkg gazebo.launch
```

## Commands used during tutorial
useful tip: press tab to auto-complete words as you type commands

To run motor controller node, open new terminal
```
cd ~/catkin_ws
source devel/setup.bash
rosrun computer_vision_pkg motor_controller
```

To run planner node, go to /src folder
```
python3 planner.py
```

To send a command to the left wheel
```
rostopic pub /left_wheel_controller/command std_msgs/Float64 "data: 1.0"
```

To send a command to the motor controller
```
rostopic pub /motor_commands std_msgs/String "data: 'LEFT'"
```

To see the ROS node tree run this command
```
rqt_graph
```
