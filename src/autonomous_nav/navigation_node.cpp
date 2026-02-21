#include <rclcpp/rclcpp.hpp>
#include <std_msgs/msg/string.hpp>
#include <sensor_msgs/msg/laser_scan.hpp>
#include <nav_msgs/msg/odometry.hpp>
#include <geometry_msgs/msg/twist.hpp>

class AutonomousNavNode : public rclcpp::Node
{
public:
  AutonomousNavNode()
  : Node("autonomous_nav_node")
  {
    // Publishers
    status_pub_ = this->create_publisher<std_msgs::msg::String>("nav_status", 10);
    cmd_vel_pub_ = this->create_publisher<geometry_msgs::msg::Twist>("cmd_vel", 10);

    // Subscribers
    scan_sub_ = this->create_subscription<sensor_msgs::msg::LaserScan>(
      "scan", 10, std::bind(&AutonomousNavNode::scan_callback, this, std::placeholders::_1));
    odom_sub_ = this->create_subscription<nav_msgs::msg::Odometry>(
      "odom", 10, std::bind(&AutonomousNavNode::odom_callback, this, std::placeholders::_1));

    timer_ = this->create_wall_timer(
      std::chrono::milliseconds(500), std::bind(&AutonomousNavNode::timer_callback, this));
    
    RCLCPP_INFO(this->get_logger(), "DeepMine AI: Autonomous Navigation Node Initialized (LiDAR Ready).");
  }

private:
  void scan_callback(const sensor_msgs::msg::LaserScan::SharedPtr msg)
  {
    // Basic Obstacle Detection: Find minimum distance in the scan range
    float min_range = msg->range_max;
    for (size_t i = 0; i < msg->ranges.size(); ++i) {
      if (msg->ranges[i] < min_range && msg->ranges[i] > msg->range_min) {
        min_range = msg->ranges[i];
      }
    }

    obstacle_detected_ = (min_range < 1.0); // 1 meter threshold
    if (obstacle_detected_) {
        RCLCPP_WARN(this->get_logger(), "OBSTACLE DETECTED! Min distance: %.2f m", min_range);
    }
  }

  void odom_callback(const nav_msgs::msg::Odometry::SharedPtr msg)
  {
    current_x_ = msg->pose.pose.position.x;
    current_y_ = msg->pose.pose.position.y;
  }

  void timer_callback()
  {
    auto status_msg = std_msgs::msg::String();
    auto cmd_msg = geometry_msgs::msg::Twist();

    if (obstacle_detected_) {
        status_msg.data = "STATUS: Obstacle Avoidance Manoeuvre";
        cmd_msg.angular.z = 0.5; // Turn
        cmd_msg.linear.x = 0.0;
    } else {
        status_msg.data = "STATUS: Navigating to Mineral Zone";
        cmd_msg.linear.x = 0.2; // Move forward
        cmd_msg.angular.z = 0.0;
    }

    RCLCPP_INFO(this->get_logger(), "DeepMine Navigation [%.1f, %.1f]: %s", current_x_, current_y_, status_msg.data.c_str());
    status_pub_->publish(status_msg);
    cmd_vel_pub_->publish(cmd_msg);
  }

  // ROS Interfaces
  rclcpp::TimerBase::SharedPtr timer_;
  rclcpp::Publisher<std_msgs::msg::String>::SharedPtr status_pub_;
  rclcpp::Publisher<geometry_msgs::msg::Twist>::SharedPtr cmd_vel_pub_;
  rclcpp::Subscription<sensor_msgs::msg::LaserScan>::SharedPtr scan_sub_;
  rclcpp::Subscription<nav_msgs::msg::Odometry>::SharedPtr odom_sub_;

  // State
  bool obstacle_detected_ = false;
  float current_x_ = 0.0;
  float current_y_ = 0.0;
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<AutonomousNavNode>());
  rclcpp::shutdown();
  return 0;
}
