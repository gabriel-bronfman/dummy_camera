import rclpy
from rclpy.duration import Duration
from rclpy.node import Node
from sensor_msgs.msg import Image
import os 
import cv2 as cv
from cv_bridge import CvBridge
from rclpy.qos import qos_profile_sensor_data

class viewer(Node):

    def __init__(self):
        super().__init__('viewer')

        self.image_sub = self.create_subscription(
            Image,
            'camera_output',
            self.image_callback,
            10)
        
        self.br = CvBridge()
        
    def image_callback(self, msg):
        try:
            cv_image = self.br.imgmsg_to_cv2(msg, "bgr8")
        except CvBridge.CvBridgeError as e:
            print("Error with bridge: " + e)
            return
        
        cv.imshow("image",cv_image)
        cv.waitKey(1)

def main(args=None):

    rclpy.init(args=args)

    viewer_node = viewer()

    rclpy.spin(viewer_node)
    rclpy.shutdown()

