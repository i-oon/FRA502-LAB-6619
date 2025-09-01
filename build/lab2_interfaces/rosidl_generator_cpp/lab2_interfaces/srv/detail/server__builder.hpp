// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from lab2_interfaces:srv/Server.idl
// generated code does not contain a copyright notice

#ifndef LAB2_INTERFACES__SRV__DETAIL__SERVER__BUILDER_HPP_
#define LAB2_INTERFACES__SRV__DETAIL__SERVER__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "lab2_interfaces/srv/detail/server__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace lab2_interfaces
{

namespace srv
{

namespace builder
{

class Init_Server_Request_target
{
public:
  Init_Server_Request_target()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::lab2_interfaces::srv::Server_Request target(::lab2_interfaces::srv::Server_Request::_target_type arg)
  {
    msg_.target = std::move(arg);
    return std::move(msg_);
  }

private:
  ::lab2_interfaces::srv::Server_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::lab2_interfaces::srv::Server_Request>()
{
  return lab2_interfaces::srv::builder::Init_Server_Request_target();
}

}  // namespace lab2_interfaces


namespace lab2_interfaces
{

namespace srv
{


}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::lab2_interfaces::srv::Server_Response>()
{
  return ::lab2_interfaces::srv::Server_Response(rosidl_runtime_cpp::MessageInitialization::ZERO);
}

}  // namespace lab2_interfaces

#endif  // LAB2_INTERFACES__SRV__DETAIL__SERVER__BUILDER_HPP_
