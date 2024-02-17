# dummy_camera

Created a basic package to pipe videos into a ROS2 graph. Images and videos are stored in a "Videos" folder in the base ws, and will be piped into a "camera_output" topic, 
that publishes sensor_msgs/Images. 

You can create a .YAML for parameters to specify videos at launch under the parameter title "file_name". You can decleare which mode the node boots up into with the parameter
"mode", with it either being video or image.

## Installation
```
git clone git@github.com:gabriel-bronfman/dummy_camera.git
cd dummy_camera
colcon build
sh ./install/local_setup.bash
```

## Run
```
ros2 run dummy_camera_pkg dummy_camera_node camera_viewer
```