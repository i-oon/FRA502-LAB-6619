// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from robot_interfaces:srv/RandomEndEffector.idl
// generated code does not contain a copyright notice

#ifndef ROBOT_INTERFACES__SRV__DETAIL__RANDOM_END_EFFECTOR__STRUCT_H_
#define ROBOT_INTERFACES__SRV__DETAIL__RANDOM_END_EFFECTOR__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/RandomEndEffector in the package robot_interfaces.
typedef struct robot_interfaces__srv__RandomEndEffector_Request
{
  uint8_t structure_needs_at_least_one_member;
} robot_interfaces__srv__RandomEndEffector_Request;

// Struct for a sequence of robot_interfaces__srv__RandomEndEffector_Request.
typedef struct robot_interfaces__srv__RandomEndEffector_Request__Sequence
{
  robot_interfaces__srv__RandomEndEffector_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} robot_interfaces__srv__RandomEndEffector_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'position'
#include "geometry_msgs/msg/detail/point__struct.h"
// Member 'orientation'
#include "geometry_msgs/msg/detail/quaternion__struct.h"

/// Struct defined in srv/RandomEndEffector in the package robot_interfaces.
typedef struct robot_interfaces__srv__RandomEndEffector_Response
{
  geometry_msgs__msg__Point position;
  geometry_msgs__msg__Quaternion orientation;
  bool success;
} robot_interfaces__srv__RandomEndEffector_Response;

// Struct for a sequence of robot_interfaces__srv__RandomEndEffector_Response.
typedef struct robot_interfaces__srv__RandomEndEffector_Response__Sequence
{
  robot_interfaces__srv__RandomEndEffector_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} robot_interfaces__srv__RandomEndEffector_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // ROBOT_INTERFACES__SRV__DETAIL__RANDOM_END_EFFECTOR__STRUCT_H_
