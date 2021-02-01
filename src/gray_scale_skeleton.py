#!/usr/bin/env python

'''
todo: 
1. import all necessary things
2. implement service server and callback 
3. add necessary publishers and subscribers
4. implement convert to grayscale
5. implement subscriber callback
'''

class Gray_Scale():
    def __init__(self):
        rospy.init_node("gray_scale", anonymous=True)
        # services

        # subscribers

        # publishers

        # other

    # will start/stop gray scale conversion based on req
    def perception_service_cb(self, req):
        pass

    # will take in compressed image and will return a compressed gray scale image
    def convert_to_grayscale(self, compressed_image_msg):
        pass

    # associated with a subscriber, will convert msg to gray scale and publish back out
    def video_cb(self, msg):
        pass

    def run(self):
        rate = rospy.Rate(10) # 10hz default
        while not rospy.is_shutdown(): 
            rate.sleep()

if __name__ == "__main__":
    gray_scale = Gray_Scale()
    gray_scale.run()