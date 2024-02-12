import rclpy
from rclpy.duration import Duration
from rclpy.node import Node
from sensor_msgs.msg import Image
import os 
import cv2 as cv
from cv_bridge import CvBridge


class dummy_camera_node(Node):

    def __init__(self):
        super().__init__('dummy_camera_node')
        
        #CV bridge used for converting CV::Mats to sensor_msg/Image
        self.br = CvBridge()

        # Create parameter that can be specified at Runtime
        self.declare_parameter('file_name', 'ROS.png')
        self.declare_parameter('mode', 'image')

        # Create path to video and video object
        video_name = self.get_parameter('file_name').get_parameter_value().string_value
        self.video_path = os.path.join('/home/gabe/experimentalros2_ws/videos', video_name)
        if (self.get_parameter('mode').get_parameter_value().string_value == 'video'):
            self.data = cv.CaptureVideo(self.video_path)
        else:
            self.data = cv.imread(self.video_path)

        #Create required publisher for pushing and timer for timing sending frames
        self.image_pub = self.create_publisher(Image,'camera_output', 10)
        self.timer = self.create_timer(.033, self.publish_cycle)
        if self.data is not None:
            self.get_logger().info("I have located the image")

    def publish_cycle(self):
        
        if (self.get_parameter('mode').get_parameter_value().string_value == 'image'):
            self.image_pub.publish(self.br.cv2_to_imgmsg(self.data, "bgr8"))
            return;
        
        try:
            ret, frame = self.video.read()
        except cv.error as e:
            self.get_logger().error('CV Error: ' + e)
            return
        
        self.image_pub.publish(self.br.cv2_to_imgmsg(self.data))
    
def main(args=None):
    rclpy.init(args=args)

    dummy_camera_node = dummy_camera()

    rclpy.spin(dummy_camera_node)
    
    dummy_camera_node.destroy_node()
    rclpy.shutdown();

if __name__ == "__main__":
    main()
