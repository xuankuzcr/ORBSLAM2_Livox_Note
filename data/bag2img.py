
# coding:utf-8
#!/usr/bin/python
 
# Extract images from a bag file.
 
#PKG = 'beginner_tutorials'
import roslib;   #roslib.load_manifest(PKG)
import rosbag
import rospy
import cv2
import sys

from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from cv_bridge import CvBridgeError
 
# Reading bag filename from command line or roslaunch parameter.
#import os
#import sys
 
rgb_path = '/home/chunran/zcr/data/rgb/'
depth_path= '/home/zyw/bag/light_depth/'
class ImageCreator():
 
 
    # def __init__(self, bag_path, rgb_topic, depth_topic, rgb_path, depth_path):
    def __init__(self):
        self.bridge = CvBridge()
        #print("11111")
        with rosbag.Bag('/home/chunran/zcr/data/rosbag/0.bag', 'r') as bag:  #要读取的bag文件;
	    num = 0
            for topic,msg,t in bag.read_messages():
                if topic == "/camera/image_color": #图像的topic
			num = num + 1
			if (num%2) == 0:
				continue
                        try:
                            cv_image = self.bridge.imgmsg_to_cv2(msg,"bgr8")
                        except CvBridgeError as e:
                            print e
	            	timestr = "%.6f" %  msg.header.stamp.to_sec()
	            	#%.6f表示小数点后带有6位，可根据精确度需要修改；
	            	image_name = timestr+ ".png" #图像命名：时间戳.png
	            	#cv_image = cv2.resize(cv_image,(640,512),0,0,interpolation=cv2.INTER_NEAREST)
	            	cv2.imwrite(rgb_path + image_name, cv_image)  #保存
            
 
if __name__ == '__main__':
 
    #rospy.init_node(PKG)
    # if len(sys.argv) < 6:
    #     usage = "Usage: python bag2img.py bag_path /topic_rgb /topic_depth rgb_out_path depth_out_path "
    #     print usage
    # else:
    #     param = str(sys.argv)
    #     bag_path = param[1]
    #     rgb_topic = param[2]
    #     depth_topic = param[3]
    #     rgb_path = param[4]
    #     depth_path = param[5]

    #     print(param)

    try:
        # image_creator = ImageCreator(bag_path, rgb_topic, depth_topic, rgb_path, depth_path)
        image_creator = ImageCreator()
    except rospy.ROSInterruptException:
        pass
