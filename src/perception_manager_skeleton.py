#!/usr/bin/env python

'''
todo: 
1. import all necessary things
2. implement service client
3. implement start and stop perception methods
4. implement timer logic in run method
'''

class Perception_Manager:


    def __init__(self):

        rospy.init_node("perception_manager", anonymous=True)

        # timer variables

        # service client stuff

    # will call the service to start gray scale conversion
    def start_gray_scale(self):
        pass

    # will call the service to stop gray scale conversion
    def stop_gray_scale(self):
        pass

    def run(self):
        rate = rospy.Rate(10) # 10hz default
        while not rospy.is_shutdown(): 

            # timer logic to convert to gray scale for 30 seconds
            
            rate.sleep()

if __name__ == "__main__":
    Perception_Manager = Perception_Manager()
    Perception_Manager.run()