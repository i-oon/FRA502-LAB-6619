// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from robot_interfaces:srv/InverseKinematic.idl
// generated code does not contain a copyright notice

#ifndef ROBOT_INTERFACES__SRV__DETAIL__INVERSE_KINEMATIC__STRUCT_H_
#define ROBOT_INTERFACES__SRV__DETAIL__INVERSE_KINEMATIC__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'target'
#include "geometry_msgs/msg/detail/point__struct.h"

/// Struct defined in srv/InverseKinematic in the package robot_interfaces.
typedef struct robot_interfaces__srv__InverseKinematic_Request
{
  geometry_msgs__msg__Point target;
} robot_interfaces__srv__InverseKinematic_Request;

// Struct for a sequence of robot_interfaces__srv__InverseKinematic_Request.
typedef struct robot_interfaces__srv__InverseKinematic_Request__Sequence
{
  robot_interfaces__srv__InverseKinematic_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} robot_interfaces__srv__InverseKinematic_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'message'
#include "rosidl_runtime_c/string.h"
// Member 'solution'
#include "rosidl_runtime_c/primitives_sequence.h"

/// Struct defined in srv/InverseKinematic in the package robot_interfaces.
typedef struct robot_interfaces__srv__InverseKinematic_Response
{
  bool success;
  rosidl_runtime_c__String message;
  rosidl_runtime_c__double__Sequence solution;
} robot_interfaces__srv__InverseKinematic_Response;

// Struct for a sequence of robot_interfaces__srv__InverseKinematic_Response.
typedef struct robot_interfaces__srv__InverseKinematic_Response__Sequence
{
  robot_interfaces__srv__InverseKinematic_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} robot_interfaces__srv__InverseKinematic_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // ROBOT_INTERFACES__SRV__DETAIL__INVERSE_KINEMATIC__STRUCT_H_
