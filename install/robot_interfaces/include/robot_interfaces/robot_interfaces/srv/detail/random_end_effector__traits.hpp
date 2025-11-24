// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from robot_interfaces:srv/RandomEndEffector.idl
// generated code does not contain a copyright notice

#ifndef ROBOT_INTERFACES__SRV__DETAIL__RANDOM_END_EFFECTOR__TRAITS_HPP_
#define ROBOT_INTERFACES__SRV__DETAIL__RANDOM_END_EFFECTOR__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "robot_interfaces/srv/detail/random_end_effector__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace robot_interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const RandomEndEffector_Request & msg,
  std::ostream & out)
{
  (void)msg;
  out << "null";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const RandomEndEffector_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  (void)msg;
  (void)indentation;
  out << "null\n";
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const RandomEndEffector_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace robot_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use robot_interfaces::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const robot_interfaces::srv::RandomEndEffector_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  robot_interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use robot_interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const robot_interfaces::srv::RandomEndEffector_Request & msg)
{
  return robot_interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<robot_interfaces::srv::RandomEndEffector_Request>()
{
  return "robot_interfaces::srv::RandomEndEffector_Request";
}

template<>
inline const char * name<robot_interfaces::srv::RandomEndEffector_Request>()
{
  return "robot_interfaces/srv/RandomEndEffector_Request";
}

template<>
struct has_fixed_size<robot_interfaces::srv::RandomEndEffector_Request>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<robot_interfaces::srv::RandomEndEffector_Request>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<robot_interfaces::srv::RandomEndEffector_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'position'
#include "geometry_msgs/msg/detail/point__traits.hpp"
// Member 'orientation'
#include "geometry_msgs/msg/detail/quaternion__traits.hpp"

namespace robot_interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const RandomEndEffector_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: position
  {
    out << "position: ";
    to_flow_style_yaml(msg.position, out);
    out << ", ";
  }

  // member: orientation
  {
    out << "orientation: ";
    to_flow_style_yaml(msg.orientation, out);
    out << ", ";
  }

  // member: success
  {
    out << "success: ";
    rosidl_generator_traits::value_to_yaml(msg.success, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const RandomEndEffector_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: position
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "position:\n";
    to_block_style_yaml(msg.position, out, indentation + 2);
  }

  // member: orientation
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "orientation:\n";
    to_block_style_yaml(msg.orientation, out, indentation + 2);
  }

  // member: success
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "success: ";
    rosidl_generator_traits::value_to_yaml(msg.success, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const RandomEndEffector_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace robot_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use robot_interfaces::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const robot_interfaces::srv::RandomEndEffector_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  robot_interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use robot_interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const robot_interfaces::srv::RandomEndEffector_Response & msg)
{
  return robot_interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<robot_interfaces::srv::RandomEndEffector_Response>()
{
  return "robot_interfaces::srv::RandomEndEffector_Response";
}

template<>
inline const char * name<robot_interfaces::srv::RandomEndEffector_Response>()
{
  return "robot_interfaces/srv/RandomEndEffector_Response";
}

template<>
struct has_fixed_size<robot_interfaces::srv::RandomEndEffector_Response>
  : std::integral_constant<bool, has_fixed_size<geometry_msgs::msg::Point>::value && has_fixed_size<geometry_msgs::msg::Quaternion>::value> {};

template<>
struct has_bounded_size<robot_interfaces::srv::RandomEndEffector_Response>
  : std::integral_constant<bool, has_bounded_size<geometry_msgs::msg::Point>::value && has_bounded_size<geometry_msgs::msg::Quaternion>::value> {};

template<>
struct is_message<robot_interfaces::srv::RandomEndEffector_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<robot_interfaces::srv::RandomEndEffector>()
{
  return "robot_interfaces::srv::RandomEndEffector";
}

template<>
inline const char * name<robot_interfaces::srv::RandomEndEffector>()
{
  return "robot_interfaces/srv/RandomEndEffector";
}

template<>
struct has_fixed_size<robot_interfaces::srv::RandomEndEffector>
  : std::integral_constant<
    bool,
    has_fixed_size<robot_interfaces::srv::RandomEndEffector_Request>::value &&
    has_fixed_size<robot_interfaces::srv::RandomEndEffector_Response>::value
  >
{
};

template<>
struct has_bounded_size<robot_interfaces::srv::RandomEndEffector>
  : std::integral_constant<
    bool,
    has_bounded_size<robot_interfaces::srv::RandomEndEffector_Request>::value &&
    has_bounded_size<robot_interfaces::srv::RandomEndEffector_Response>::value
  >
{
};

template<>
struct is_service<robot_interfaces::srv::RandomEndEffector>
  : std::true_type
{
};

template<>
struct is_service_request<robot_interfaces::srv::RandomEndEffector_Request>
  : std::true_type
{
};

template<>
struct is_service_response<robot_interfaces::srv::RandomEndEffector_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // ROBOT_INTERFACES__SRV__DETAIL__RANDOM_END_EFFECTOR__TRAITS_HPP_
