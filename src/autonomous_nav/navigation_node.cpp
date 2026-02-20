#include <rclcpp/rclcpp.hpp>
#include <std_msgs/msg/string.hpp>

class AutonomousNavNode : public rclcpp::Node
{
public:
  AutonomousNavNode()
  : Node("autonomous_nav_node")
  {
    publisher_ = this->create_publisher<std_msgs::msg::String>("nav_status", 10);
    timer_ = this->create_wall_timer(
      std::chrono::milliseconds(500), std::bind(&AutonomousNavNode::timer_callback, this));
    RCLCPP_INFO(this->get_logger(), "Autonomous Navigation Node Started.");
  }

private:
  void timer_callback()
  {
    auto message = std_msgs::msg::String();
    message.data = "Navigating to waypoint [X: 10.5, Y: 20.3, Z: -50.0]";
    RCLCPP_INFO(this->get_logger(), "Publishing: '%s'", message.data.c_str());
    publisher_->publish(message);
  }
  rclcpp::TimerBase::SharedPtr timer_;
  rclcpp::Publisher<std_msgs::msg::String>::SharedPtr publisher_;
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<AutonomousNavNode>());
  rclcpp::shutdown();
  return 0;
}
