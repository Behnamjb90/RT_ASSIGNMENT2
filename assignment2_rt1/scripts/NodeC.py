#! /usr/bin/env python3
#=======================================================================================
#   ________  ________  _________  _______   _____ ______   ___  ________      
#  |\   __  \|\   __  \|\___   ___\\  ___ \ |\   _ \  _   \|\  \|\   ____\     
#  \ \  \|\  \ \  \|\  \|___ \  \_\ \   __/|\ \  \\\__\ \  \ \  \ \  \___|_    
#   \ \   __  \ \   _  _\   \ \  \ \ \  \_|/_\ \  \\|__| \  \ \  \ \_____  \   
#    \ \  \ \  \ \  \\  \|   \ \  \ \ \  \_|\ \ \  \    \ \  \ \  \|____|\  \  
#     \ \__\ \__\ \__\\ _\    \ \__\ \ \_______\ \__\    \ \__\ \__\____\_\  \ 
#      \|__|\|__|\|__|\|__|    \|__|  \|_______|\|__|     \|__|\|__|\_________\
#                                                                  \|_________|
#                             ROBOTIC GROUP                     
#                                                                              
#========================================================================================

# Import necessary libraries
import math
from assignment2_rt1.msg import odom_custom_msg
import rospy

# Initialize variables and flags
start_description_flag=1
cou =0
velocity =0
velocity_avg =0
goal_distance =0


# Callback function for subscriber
def callback_subscriber(data):

    # Access global variables
    global cou
    global velocity
    global velocity_avg
    global goal_distance

    # Get desired position from parameters
    goal_pos_x = rospy.get_param("/des_pos_x")
    goal_pos_y = rospy.get_param("/des_pos_y")

    # Get current position from subscriber
    current_pos_x = data.x
    current_pos_y = data.y

    # Calculate distance to target position
    goal_distance= math.sqrt(((goal_pos_x - current_pos_x)**2)+((goal_pos_y - current_pos_y)**2))

    # Get current velocity from subscriber
    current_vel_x = data.vel_x
    current_vel_y = data.vel_y

    current_vel= math.sqrt(( current_vel_x**2)+(current_vel_y**2))

    # Calculate average velocity
    if cou<10:
        velocity=velocity+current_vel
        cou +=1
    elif cou==10:
        cou=0
        velocity /= 10
        velocity_avg=velocity
        velocity=0



# Main function
if __name__ == "__main__":
    rospy.logwarn("Node C is running")


    # Initialize node
    rospy.init_node('NodeC')

    # Get print interval parameter from launch file
    refresh_speed=rospy.get_param("/print_interval")
    sleep_rate = rospy.Rate(refresh_speed)

    # Subscribe to topic
    rospy.Subscriber("position_and_velocity", odom_custom_msg, callback_subscriber)

    # Loop until node is shut down
    while not rospy.is_shutdown():
        # Print information      
        print(f"Distance of robot to target: {goal_distance : .3f}")
        print(f'Average velocity of robot: {velocity_avg: .3f}')
        print(f"---------------------------")
  
        sleep_rate.sleep()

