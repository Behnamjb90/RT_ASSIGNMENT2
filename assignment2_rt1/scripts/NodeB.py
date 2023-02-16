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


import rospy
from std_srvs.srv import Empty, EmptyResponse
import assignment_2_2022.msg


# Initialize counters and a sequence number
reached_goal = 0
canceled_goal = 0

# Callback function for service
# This function is called when the service is requested
def callback_service(req):

    global canceled_goal , reached_goal 
    print("-------------------------------------")
    print(f"\nNumber of canceled goal: {canceled_goal}")
    print(f"\nnumber of reached goal: {reached_goal}")

    return EmptyResponse()

# Callback function for subscriber 
# This function is called when a message is received from the /reaching_goal/result topic
def callback_subscriber(data):
    if data.status.status == 2:
        global canceled_goal
        canceled_goal += 1
    
    elif data.status.status == 3:
        global reached_goal
        reached_goal += 1



if __name__ == "__main__":


    
    rospy.logwarn("Node B is running")

    # Initialize the node
    rospy.init_node('NodeB')

    # Subscribe to the /reaching_goal/result topic
    rospy.Subscriber("/reaching_goal/result", assignment_2_2022.msg.PlanningActionResult, callback_subscriber)

    # Initialize the service
    rospy.Service('reach_cancel_ints', Empty, callback_service)

    # Set the rate of the loop to 1Hz
    sleep_rate = rospy.Rate(1)

    # Run the loop until the node is shutdown
    while not rospy.is_shutdown():


        print("waiting for a client to call the service ...")   
        
        # Sleep for the remaining time to achieve 1Hz
        sleep_rate.sleep()
