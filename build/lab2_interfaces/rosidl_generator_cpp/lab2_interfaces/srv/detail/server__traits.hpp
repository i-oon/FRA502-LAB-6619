// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from lab2_interfaces:srv/Server.idl
// generated code does not contain a copyright notice

#ifndef LAB2_INTERFACES__SRV__DETAIL__SERVER__TRAITS_HPP_
#define LAB2_INTERFACES__SRV__DETAIL__SERVER__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "lab2_interfaces/srv/detail/server__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'target'
#include "geometry_msgs/msg/detail/point__traits.hpp"

namespace lab2_interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const Server_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: target
  {
    out << "target: ";
    to_flow_style_yaml(msg.target, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Server_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: target
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "target:\n";
    to_block_style_yaml(msg.target, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Server_Request & msg, bool use_flow_style = false)
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

}  // namespace lab2_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use lab2_interfaces::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const lab2_interfaces::srv::Server_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  lab2_interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use lab2_interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const lab2_interfaces::srv::Server_Request & msg)
{
  return lab2_interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<lab2_interfaces::srv::Server_Request>()
{
  return "lab2_interfaces::srv::Server_Request";
}

template<>
inline const char * name<lab2_interfaces::srv::Server_Request>()
{
  return "lab2_interfaces/srv/Server_Request";
}

template<>
struct has_fixed_size<lab2_interfaces::srv::Server_Request>
  : std::integral_constant<bool, has_fixed_size<geometry_msgs::msg::Point>::value> {};

template<>
struct has_bounded_size<lab2_interfaces::srv::Server_Request>
  : std::integral_constant<bool, has_bounded_size<geometry_msgs::msg::Point>::value> {};

template<>
struct is_message<lab2_interfaces::srv::Server_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace lab2_interfaces
{

namespace srv
{

inline void to_flow_style_yaml(
  const Server_Response & msg,
  std::ostream & out)
{
  (void)msg;
  out << "null";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Server_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  (void)msg;
  (void)indentation;
  out << "null\n";
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Server_Response & msg, bool use_flow_style = false)
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

}  // namespace lab2_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use lab2_interfaces::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const lab2_interfaces::srv::Server_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  lab2_interfaces::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use lab2_interfaces::srv::to_yaml() instead")]]
inline std::string to_yaml(const lab2_interfaces::srv::Server_Response & msg)
{
  return lab2_interfaces::srv::to_yaml(msg);
}

template<>
inline const char * data_type<lab2_interfaces::srv::Server_Response>()
{
  return "lab2_interfaces::srv::Server_Response";
}

template<>
inline const char * name<lab2_interfaces::srv::Server_Response>()
{
  return "lab2_interfaces/srv/Server_Response";
}

template<>
struct has_fixed_size<lab2_interfaces::srv::Server_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<lab2_interfaces::srv::Server_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<lab2_interfaces::srv::Server_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<lab2_interfaces::srv::Server>()
{
  return "lab2_interfaces::srv::Server";
}

template<>
inline const char * name<lab2_interfaces::srv::Server>()
{
  return "lab2_interfaces/srv/Server";
}

template<>
struct has_fixed_size<lab2_interfaces::srv::Server>
  : std::integral_constant<
    bool,
    has_fixed_size<lab2_interfaces::srv::Server_Request>::value &&
    has_fixed_size<lab2_interfaces::srv::Server_Response>::value
  >
{
};

template<>
struct has_bounded_size<lab2_interfaces::srv::Server>
  : std::integral_constant<
    bool,
    has_bounded_size<lab2_interfaces::srv::Server_Request>::value &&
    has_bounded_size<lab2_interfaces::srv::Server_Response>::value
  >
{
};

template<>
struct is_service<lab2_interfaces::srv::Server>
  : std::true_type
{
};

template<>
struct is_service_request<lab2_interfaces::srv::Server_Request>
  : std::true_type
{
};

template<>
struct is_service_response<lab2_interfaces::srv::Server_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // LAB2_INTERFACES__SRV__DETAIL__SERVER__TRAITS_HPP_
