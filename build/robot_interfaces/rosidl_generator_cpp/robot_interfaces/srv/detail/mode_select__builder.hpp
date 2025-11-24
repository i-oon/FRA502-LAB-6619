// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from robot_interfaces:srv/ModeSelect.idl
// generated code does not contain a copyright notice

#ifndef ROBOT_INTERFACES__SRV__DETAIL__MODE_SELECT__BUILDER_HPP_
#define ROBOT_INTERFACES__SRV__DETAIL__MODE_SELECT__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "robot_interfaces/srv/detail/mode_select__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace robot_interfaces
{

namespace srv
{

namespace builder
{

class Init_ModeSelect_Request_mode
{
public:
  Init_ModeSelect_Request_mode()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::robot_interfaces::srv::ModeSelect_Request mode(::robot_interfaces::srv::ModeSelect_Request::_mode_type arg)
  {
    msg_.mode = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robot_interfaces::srv::ModeSelect_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::robot_interfaces::srv::ModeSelect_Request>()
{
  return robot_interfaces::srv::builder::Init_ModeSelect_Request_mode();
}

}  // namespace robot_interfaces


namespace robot_interfaces
{

namespace srv
{

namespace builder
{

class Init_ModeSelect_Response_message
{
public:
  explicit Init_ModeSelect_Response_message(::robot_interfaces::srv::ModeSelect_Response & msg)
  : msg_(msg)
  {}
  ::robot_interfaces::srv::ModeSelect_Response message(::robot_interfaces::srv::ModeSelect_Response::_message_type arg)
  {
    msg_.message = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robot_interfaces::srv::ModeSelect_Response msg_;
};

class Init_ModeSelect_Response_solution
{
public:
  explicit Init_ModeSelect_Response_solution(::robot_interfaces::srv::ModeSelect_Response & msg)
  : msg_(msg)
  {}
  Init_ModeSelect_Response_message solution(::robot_interfaces::srv::ModeSelect_Response::_solution_type arg)
  {
    msg_.solution = std::move(arg);
    return Init_ModeSelect_Response_message(msg_);
  }

private:
  ::robot_interfaces::srv::ModeSelect_Response msg_;
};

class Init_ModeSelect_Response_success
{
public:
  Init_ModeSelect_Response_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ModeSelect_Response_solution success(::robot_interfaces::srv::ModeSelect_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return Init_ModeSelect_Response_solution(msg_);
  }

private:
  ::robot_interfaces::srv::ModeSelect_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::robot_interfaces::srv::ModeSelect_Response>()
{
  return robot_interfaces::srv::builder::Init_ModeSelect_Response_success();
}

}  // namespace robot_interfaces

#endif  // ROBOT_INTERFACES__SRV__DETAIL__MODE_SELECT__BUILDER_HPP_
