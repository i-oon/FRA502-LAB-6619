// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from robot_interfaces:srv/ModeSelect.idl
// generated code does not contain a copyright notice

#ifndef ROBOT_INTERFACES__SRV__DETAIL__MODE_SELECT__STRUCT_H_
#define ROBOT_INTERFACES__SRV__DETAIL__MODE_SELECT__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'mode'
#include "std_msgs/msg/detail/string__struct.h"

/// Struct defined in srv/ModeSelect in the package robot_interfaces.
typedef struct robot_interfaces__srv__ModeSelect_Request
{
  std_msgs__msg__String mode;
} robot_interfaces__srv__ModeSelect_Request;

// Struct for a sequence of robot_interfaces__srv__ModeSelect_Request.
typedef struct robot_interfaces__srv__ModeSelect_Request__Sequence
{
  robot_interfaces__srv__ModeSelect_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} robot_interfaces__srv__ModeSelect_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'solution'
#include "rosidl_runtime_c/primitives_sequence.h"
// Member 'message'
#include "rosidl_runtime_c/string.h"

/// Struct defined in srv/ModeSelect in the package robot_interfaces.
typedef struct robot_interfaces__srv__ModeSelect_Response
{
  bool success;
  rosidl_runtime_c__double__Sequence solution;
  rosidl_runtime_c__String message;
} robot_interfaces__srv__ModeSelect_Response;

// Struct for a sequence of robot_interfaces__srv__ModeSelect_Response.
typedef struct robot_interfaces__srv__ModeSelect_Response__Sequence
{
  robot_interfaces__srv__ModeSelect_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} robot_interfaces__srv__ModeSelect_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // ROBOT_INTERFACES__SRV__DETAIL__MODE_SELECT__STRUCT_H_
