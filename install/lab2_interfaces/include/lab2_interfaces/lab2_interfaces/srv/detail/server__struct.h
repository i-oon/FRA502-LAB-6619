// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from lab2_interfaces:srv/Server.idl
// generated code does not contain a copyright notice

#ifndef LAB2_INTERFACES__SRV__DETAIL__SERVER__STRUCT_H_
#define LAB2_INTERFACES__SRV__DETAIL__SERVER__STRUCT_H_

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

/// Struct defined in srv/Server in the package lab2_interfaces.
typedef struct lab2_interfaces__srv__Server_Request
{
  geometry_msgs__msg__Point target;
} lab2_interfaces__srv__Server_Request;

// Struct for a sequence of lab2_interfaces__srv__Server_Request.
typedef struct lab2_interfaces__srv__Server_Request__Sequence
{
  lab2_interfaces__srv__Server_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} lab2_interfaces__srv__Server_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/Server in the package lab2_interfaces.
typedef struct lab2_interfaces__srv__Server_Response
{
  uint8_t structure_needs_at_least_one_member;
} lab2_interfaces__srv__Server_Response;

// Struct for a sequence of lab2_interfaces__srv__Server_Response.
typedef struct lab2_interfaces__srv__Server_Response__Sequence
{
  lab2_interfaces__srv__Server_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} lab2_interfaces__srv__Server_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // LAB2_INTERFACES__SRV__DETAIL__SERVER__STRUCT_H_
