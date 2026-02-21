import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Float32
import json
import random

class ISGMonitorNode(Node):
    """
    ROS 2 Node for monitoring environmental conditions and personnel health.
    """
    def __init__(self):
        super().__init__('isg_monitor_node')
        
        # Publishers
        self.env_pub = self.create_publisher(String, 'env_status', 10)
        self.health_pub = self.create_publisher(String, 'health_status', 10)
        
        # Thresholds
        self.thresholds = {
            "methane": 5.0, # percentage
            "co2": 1000,   # ppm
            "heart_rate_max": 120
        }
        
        self.timer = self.create_wall_timer(2.0, self.timer_callback)
        self.get_logger().info("DeepMine Smart OHS: ISG Monitoring Node Started.")

    def timer_callback(self):
        # Simulate sensor readings
        env_data = {
            "methane": random.uniform(0.0, 6.0),
            "co2": random.randint(400, 1200)
        }
        health_data = {
            "heart_rate": random.randint(60, 130),
            "location": {"lat": 36.12, "lon": 42.45}
        }

        # Publish data as JSON strings
        env_msg = String()
        env_msg.data = json.dumps(env_data)
        self.env_pub.publish(env_msg)

        health_msg = String()
        health_msg.data = json.dumps(health_data)
        self.health_pub.publish(health_msg)

        self.get_logger().info(f"Published Env Data: {env_data}")

def main(args=None):
    rclpy.init(args=args)
    node = ISGMonitorNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
