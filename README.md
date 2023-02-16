# RT_ASSIGNMENT2

[Università degli studi di Genova](https://unige.it/en/ "University of Genoa")

Professor: [Carmine Recchiuto](https://github.com/CarmineD8 "Carmine Recchiuto")

Student: Behnam Jababri kalkhoran  - S5403927 - Robotics Engineering 
----------------------------------------------------------------------------

*2nd assignment of Research Track 1* 

----------------------------------------------------------------------------
This repository contains the ROS package developed for the second assignment: *assignment2_rt1*

## Required packages
- You need to have the *konsole* application installed in your machine, since it is used to display the different terminal (*Gazebo and RVIZ*)

## creating and running the project
after installing packages you can build the package by executing the command `catkin_make` within the root directory of your workspace. (having ROS Noetic is vital)

Then, to be able to run the simulation, we first need to make executable the Python scripts corresponding to the three nodes: *nodeA.py*, *nodeB.py* and *nodeC.py*, located within the `scripts` folder. To do that, we need to go to the `scripts` folder and execute the following command:
```console
chmod +x *.py
```

At teh END, in order to run the simulation, a launch file has been created. Its name is *my_assignment_2.launch*. So, you can run the whole simulation by executing the following command:
```console
roslaunch assignment2_rt1.launch
```
The following items will run:
- **Gazebo**, for simulation of the robot .
- **RViz**, for visualize of robot.
- **nodeA**: the terminal - action client (*nodeA*).
- **nodeB**: the terminal - service node (*nodeB*).
- **nodeC**: the terminal - *nodeC*.

## Repository inside you can access :
The package *assignment2_rt1* is organized as follows:
- The `scripts` folder, which contains the Python scripts corresponding to the three nodes: *nodeA.py*, *nodeB.py* and *nodeC.py*.
- The `msg` folder, which contains the definition of the custom message 
- The `srv` folder, which contains the definition of the custom service 
- The `launch` folder, that contains the launch file (*assignment2_rt1.launch*).
- The *CMakeLists.txt* file.
- The package manifest (*package.xml*).

###### Nodes
NodeA

- A node that implements an action client, allowing the user to set a target (x, y) or cancel it. The node also publishes the robot position and velocity as a custom message (x,y, vel_x, vel_z), relying on the values published on the topic /odom. 

NodeB

- A service node that, when called, prints the number of goals reached and canceled

NodeC

- A node that subscribes to the robot’s position and velocity (using the custom message) and prints the distance of the robot from the target and the robot’s average speed.

###### Launch file

- A launch file that  starts the whole simulation. Also, in this launch file the value for the frequency at which node C publishes the information is set.


