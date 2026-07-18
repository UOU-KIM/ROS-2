

import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from std_msgs.msg import String


class HelloworldPublisher (Node):
    def __int__(self):
        super().__init__('helloworld_publisher')
        qos_profile = QoSProfile(depth=10)
        self.helloworld_publisher = self.create_publisher(String, 'helloworld', qos_profile)
        time_period_sec = 1
        self.timer = self.create_timer(time_period_sec, self.publisher_helloworld_msg)
        self.cout = 0
        
    def publisher_helloworld_msg(self):
        msg = String()
        msg.data = 'Hello World: {0}'.format(self.count)
        self.helloworld_publisher.publish(msg)
        self.get_logger().info('Published message: {0}'.format(msg.data))
        self.count +=1
        
        
def main(args = None):
    rclpy.init(args = args)
    node = HelloworldPublisher()
    
    try:
        rclpy.spin(node)
        
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrupt (SIGINT)')
        
    finally:
        node.destroy_node()
        rclpy.shutdown()
        
if __name__ == '__main__':
    main()
    
    
    
    
    