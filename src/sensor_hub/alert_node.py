import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import json

class AlertNode(Node):
    """
    Subscribes to status topics and generates safety alerts.
    """
    def __init__(self):
        super().__init__('alert_node')
        
        self.env_sub = self.create_subscription(String, 'env_status', self.env_callback, 10)
        self.health_sub = self.create_subscription(String, 'health_status', self.health_callback, 10)
        
        self.thresholds = {
            "methane": 5.0,
            "co2": 1000,
            "heart_rate_max": 120
        }
        self.get_logger().info("DeepMine Alert System: Initialized.")

    def env_callback(self, msg):
        data = json.loads(msg.data)
        if data['methane'] > self.thresholds['methane']:
            self.get_logger().error(f"DANGER: METHANE LEVEL CRITICAL: {data['methane']:.2f}%")
        if data['co2'] > self.thresholds['co2']:
            self.get_logger().warn(f"WARNING: CO2 LEVEL HIGH: {data['co2']} ppm")

    def health_callback(self, msg):
        data = json.loads(msg.data)
        if data['heart_rate'] > self.thresholds['heart_rate_max']:
            self.get_logger().error(f"EMERGENCY: ABNORMAL HEART RATE: {data['heart_rate']} bpm at site")

def main(args=None):
    rclpy.init(args=args)
    node = AlertNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
