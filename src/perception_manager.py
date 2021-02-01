#!/usr/bin/env python

'''
todo: 
1. import all necessary things
2. implement service client
3. implement start and stop perception methods
4. implement timer logic in run method
'''

import rospy
from std_srvs.srv import SetBool, SetBoolResponse

class Perception_Manager:


    def __init__(self):

        rospy.init_node("perception_manager", anonymous=True)

        self.curr_time = rospy.get_time()
        self.prev_time = float('inf')

        rospy.wait_for_service('perception_service')

        try:
            self.perception_service = rospy.ServiceProxy('perception_service', SetBool)
        except rospy.ServiceException as e:
            rospy.logwarn_once("Service call failed: %s"%e)

    def start_gray_scale(self):
        self.perception_service(True)

    def stop_gray_scale(self):
        self.perception_service(False)

    def run(self):
        rate = rospy.Rate(10) # 10hz default
        while not rospy.is_shutdown(): 
            self.curr_time = rospy.get_time()
            if(self.prev_time - self.curr_time == float('inf')):
                self.start_gray_scale()
                self.prev_time = self.curr_time
            elif(self.curr_time - self.prev_time > 30):
                self.stop_gray_scale()
                self.prev_time = self.curr_time
            # want to have timer here to do this for 30 seconds
            rate.sleep()

if __name__ == "__main__":
    Perception_Manager = Perception_Manager()
    Perception_Manager.run()