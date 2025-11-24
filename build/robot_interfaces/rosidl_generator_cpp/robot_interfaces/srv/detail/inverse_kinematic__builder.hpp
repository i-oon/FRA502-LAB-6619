// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from robot_interfaces:srv/InverseKinematic.idl
// generated code does not contain a copyright notice

#ifndef ROBOT_INTERFACES__SRV__DETAIL__INVERSE_KINEMATIC__BUILDER_HPP_
#define ROBOT_INTERFACES__SRV__DETAIL__INVERSE_KINEMATIC__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "robot_interfaces/srv/detail/inverse_kinematic__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace robot_interfaces
{

namespace srv
{

namespace builder
{

class Init_InverseKinematic_Request_target
{
public:
  Init_InverseKinematic_Request_target()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::robot_interfaces::srv::InverseKinematic_Request target(::robot_interfaces::srv::InverseKinematic_Request::_target_type arg)
  {
    msg_.target = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robot_interfaces::srv::InverseKinematic_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::robot_interfaces::srv::InverseKinematic_Request>()
{
  return robot_interfaces::srv::builder::Init_InverseKinematic_Request_target();
}

}  // namespace robot_interfaces


namespace robot_interfaces
{

namespace srv
{

namespace builder
{

class Init_InverseKinematic_Response_solution
{
public:
  explicit Init_InverseKinematic_Response_solution(::robot_interfaces::srv::InverseKinematic_Response & msg)
  : msg_(msg)
  {}
  ::robot_interfaces::srv::InverseKinematic_Response solution(::robot_interfaces::srv::InverseKinematic_Response::_solution_type arg)
  {
    msg_.solution = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robot_interfaces::srv::InverseKinematic_Response msg_;
};

class Init_InverseKinematic_Response_message
{
public:
  explicit Init_InverseKinematic_Response_message(::robot_interfaces::srv::InverseKinematic_Response & msg)
  : msg_(msg)
  {}
  Init_InverseKinematic_Response_solution message(::robot_interfaces::srv::InverseKinematic_Response::_message_type arg)
  {
    msg_.message = std::move(arg);
    return Init_InverseKinematic_Response_solution(msg_);
  }

private:
  ::robot_interfaces::srv::InverseKinematic_Response msg_;
};

class Init_InverseKinematic_Response_success
{
public:
  Init_InverseKinematic_Response_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_InverseKinematic_Response_message success(::robot_interfaces::srv::InverseKinematic_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return Init_InverseKinematic_Response_message(msg_);
  }

private:
  ::robot_interfaces::srv::InverseKinematic_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::robot_interfaces::srv::InverseKinematic_Response>()
{
  return robot_interfaces::srv::builder::Init_InverseKinematic_Response_success();
}

}  // namespace robot_interfaces

#endif  // ROBOT_INTERFACES__SRV__DETAIL__INVERSE_KINEMATIC__BUILDER_HPP_
