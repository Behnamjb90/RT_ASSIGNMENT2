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


# Import the necessary modules and message types
import rospy
from geometry_msgs.msg import PoseStamped 
import actionlib.msg 
import assignment_2_2022.msg 
import actionlib
from nav_msgs.msg import Odometry
from rt1_2nd_assignment.msg import odom_custom_msg
import os

# Define a callback function that takes odometry data and publishes it as a custom message
def callback(data):
    publisher = rospy.Publisher('position_and_velocity', odom_custom_msg, queue_size=5)
    custom_message = odom_custom_msg()
    custom_message.x = data.pose.pose.position.x
    custom_message.y = data.pose.pose.position.y
    custom_message.vel_x = data.twist.twist.linear.x
    custom_message.vel_y = data.twist.twist.linear.y
    publisher.publish(custom_message)


# Define the interface function to display a menu of options to the user
def user_interface():

    # Clear the console and display the menu options
    os.system('clear')  
    print("##    controling instruction panel           ##\n")
    print("###############################################\n")
    print("1:destination position\n")
    print("2:STOP\n")
    # Ask the user to select an operation
    user_choice = input("Select your request: ")

    # Check the user selection and call the corresponding function or raise an error
    if   (user_choice == "1"):
        set_goal()
    elif (user_choice == "2"):
        goal_cancel() 
    else:
        wrong_input()


# Define the target_client function to prompt the user for an X and Y position and send the goal to the action server
def set_goal():

    # Prompt the user for an X and Y position
    X_cordinate = input(" enter X : ")
    Y_cordinate = input(" enter Y : ")

    # Convert the user input to integers
    X_cordinate = int(X_cordinate)
    Y_cordinate = int(Y_cordinate)
    
    # Print the user input to the console
    print(f'\nX cordinate: {X_cordinate}  \n Y cordinate: {Y_cordinate}')
  


    # Wait for the action server to connect
    client.wait_for_server()
    print("\nAction server conected")

    # Create a PoseStamped message with the user input as the goal position
    pos_goal = PoseStamped()
    pos_goal.pose.position.x = X_cordinate
    pos_goal.pose.position.y = Y_cordinate

    # Create a PlanningGoal message with the PoseStamped message as the goal
    pos_goal = assignment_2_2022.msg.PlanningGoal(pos_goal)

    # Send the goal to the action server
    client.send_goal(pos_goal)
    print("\n**Goal sent**")

    rospy.sleep(2)    

    # Call the interface function
    user_interface()
      
# Define the cancel_target function to cancel the current goal
def goal_cancel():

    # Cancel the current goal and print a message to the console
    client.cancel_goal()
    print(f"\n Goal canceled by user")

    rospy.sleep(2)    

    # Call the interface function
    user_interface()

# Define the wrong function to handle incorrect user input
def wrong_input():

    # Print an error message to the console and wait for two seconds
    print("\nWrong input, please try again")
    rospy.sleep(2)

    # Call the interface function
    user_interface()




# Main function that initializes the node, subscribes to the /odom topic, initializes the action client, and starts the main loop
if __name__ == '__main__':

    rospy.logwarn("Node A is running")

    # Initialize the ROS node with the name 'NodeA'
    rospy.init_node('NodeA')
    
    # Subscribe to the '/odom' topic and specify the callback function to use
    rospy.Subscriber("/odom", Odometry, callback)

    # Create an instance of the action client to communicate with the action server
    client = actionlib.SimpleActionClient('/reaching_goal',assignment_2_2022.msg.PlanningAction )
    
    # Call the user interface function
    user_interface()

    # Run the main loop
    rospy.spin()

    

