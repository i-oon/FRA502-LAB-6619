// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from robot_interfaces:srv/RandomEndEffector.idl
// generated code does not contain a copyright notice

#ifndef ROBOT_INTERFACES__SRV__DETAIL__RANDOM_END_EFFECTOR__BUILDER_HPP_
#define ROBOT_INTERFACES__SRV__DETAIL__RANDOM_END_EFFECTOR__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "robot_interfaces/srv/detail/random_end_effector__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace robot_interfaces
{

namespace srv
{


}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::robot_interfaces::srv::RandomEndEffector_Request>()
{
  return ::robot_interfaces::srv::RandomEndEffector_Request(rosidl_runtime_cpp::MessageInitialization::ZERO);
}

}  // namespace robot_interfaces


namespace robot_interfaces
{

namespace srv
{

namespace builder
{

class Init_RandomEndEffector_Response_success
{
public:
  explicit Init_RandomEndEffector_Response_success(::robot_interfaces::srv::RandomEndEffector_Response & msg)
  : msg_(msg)
  {}
  ::robot_interfaces::srv::RandomEndEffector_Response success(::robot_interfaces::srv::RandomEndEffector_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robot_interfaces::srv::RandomEndEffector_Response msg_;
};

class Init_RandomEndEffector_Response_orientation
{
public:
  explicit Init_RandomEndEffector_Response_orientation(::robot_interfaces::srv::RandomEndEffector_Response & msg)
  : msg_(msg)
  {}
  Init_RandomEndEffector_Response_success orientation(::robot_interfaces::srv::RandomEndEffector_Response::_orientation_type arg)
  {
    msg_.orientation = std::move(arg);
    return Init_RandomEndEffector_Response_success(msg_);
  }

private:
  ::robot_interfaces::srv::RandomEndEffector_Response msg_;
};

class Init_RandomEndEffector_Response_position
{
public:
  Init_RandomEndEffector_Response_position()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_RandomEndEffector_Response_orientation position(::robot_interfaces::srv::RandomEndEffector_Response::_position_type arg)
  {
    msg_.position = std::move(arg);
    return Init_RandomEndEffector_Response_orientation(msg_);
  }

private:
  ::robot_interfaces::srv::RandomEndEffector_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::robot_interfaces::srv::RandomEndEffector_Response>()
{
  return robot_interfaces::srv::builder::Init_RandomEndEffector_Response_position();
}

}  // namespace robot_interfaces

#endif  // ROBOT_INTERFACES__SRV__DETAIL__RANDOM_END_EFFECTOR__BUILDER_HPP_
