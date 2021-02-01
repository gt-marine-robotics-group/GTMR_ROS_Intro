#!/usr/bin/env python

'''
todo: 
1. import all necessary things
2. implement service server and callback
3. add necessary publishers and subscribers
4. implement convert to grayscale
5. implement subscriber callback
'''

import rospy
from std_srvs.srv import SetBool, SetBoolResponse
import cv2
from cv_bridge import CvBridge
from sensor_msgs.msg import Image, CompressedImage

class Gray_Scale():
    def __init__(self):

        self.enabled = False

        rospy.init_node("gray_scale", anonymous=True)
        # services
        s = rospy.Service('perception_service', SetBool, self.perception_service_cb)
        # subscribers
        # subscriber for camera feed
        self.subVideo = rospy.Subscriber("/camera/image_raw/compressed", CompressedImage, self.video_cb)
        # publishers
        self.pub_pose = rospy.Publisher("/gray_scale_out/compressed", CompressedImage, queue_size=1)
        self.bridge = CvBridge()

    def perception_service_cb(self, req):
        self.enabled = req.data
        return SetBoolResponse(True, "Yay!")

    def convert_to_grayscale(self, compressed_image_msg):
        cv_image = self.bridge.compressed_imgmsg_to_cv2(compressed_image_msg)
        cv_gray_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
        gray_image_msg = self.bridge.cv2_to_compressed_imgmsg(cv_gray_image)
        return gray_image_msg

    def video_cb(self, msg):
        if(self.enabled):
            gray_msg = self.convert_to_grayscale(msg)
            self.pub_pose.publish(gray_msg)

    def run(self):
        rate = rospy.Rate(10) # 10hz default
        while not rospy.is_shutdown(): 
            rospy.loginfo_throttle(0.5,'enabled: ' + str(self.enabled))
            rate.sleep()

if __name__ == "__main__":
    gray_scale = Gray_Scale()
    gray_scale.run()