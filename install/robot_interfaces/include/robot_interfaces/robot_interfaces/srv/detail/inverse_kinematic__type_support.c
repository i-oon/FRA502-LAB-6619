// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from robot_interfaces:srv/InverseKinematic.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "robot_interfaces/srv/detail/inverse_kinematic__rosidl_typesupport_introspection_c.h"
#include "robot_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "robot_interfaces/srv/detail/inverse_kinematic__functions.h"
#include "robot_interfaces/srv/detail/inverse_kinematic__struct.h"


// Include directives for member types
// Member `target`
#include "geometry_msgs/msg/point.h"
// Member `target`
#include "geometry_msgs/msg/detail/point__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void robot_interfaces__srv__InverseKinematic_Request__rosidl_typesupport_introspection_c__InverseKinematic_Request_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  robot_interfaces__srv__InverseKinematic_Request__init(message_memory);
}

void robot_interfaces__srv__InverseKinematic_Request__rosidl_typesupport_introspection_c__InverseKinematic_Request_fini_function(void * message_memory)
{
  robot_interfaces__srv__InverseKinematic_Request__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember robot_interfaces__srv__InverseKinematic_Request__rosidl_typesupport_introspection_c__InverseKinematic_Request_message_member_array[1] = {
  {
    "target",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(robot_interfaces__srv__InverseKinematic_Request, target),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers robot_interfaces__srv__InverseKinematic_Request__rosidl_typesupport_introspection_c__InverseKinematic_Request_message_members = {
  "robot_interfaces__srv",  // message namespace
  "InverseKinematic_Request",  // message name
  1,  // number of fields
  sizeof(robot_interfaces__srv__InverseKinematic_Request),
  robot_interfaces__srv__InverseKinematic_Request__rosidl_typesupport_introspection_c__InverseKinematic_Request_message_member_array,  // message members
  robot_interfaces__srv__InverseKinematic_Request__rosidl_typesupport_introspection_c__InverseKinematic_Request_init_function,  // function to initialize message memory (memory has to be allocated)
  robot_interfaces__srv__InverseKinematic_Request__rosidl_typesupport_introspection_c__InverseKinematic_Request_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t robot_interfaces__srv__InverseKinematic_Request__rosidl_typesupport_introspection_c__InverseKinematic_Request_message_type_support_handle = {
  0,
  &robot_interfaces__srv__InverseKinematic_Request__rosidl_typesupport_introspection_c__InverseKinematic_Request_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_robot_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, robot_interfaces, srv, InverseKinematic_Request)() {
  robot_interfaces__srv__InverseKinematic_Request__rosidl_typesupport_introspection_c__InverseKinematic_Request_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, geometry_msgs, msg, Point)();
  if (!robot_interfaces__srv__InverseKinematic_Request__rosidl_typesupport_introspection_c__InverseKinematic_Request_message_type_support_handle.typesupport_identifier) {
    robot_interfaces__srv__InverseKinematic_Request__rosidl_typesupport_introspection_c__InverseKinematic_Request_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &robot_interfaces__srv__InverseKinematic_Request__rosidl_typesupport_introspection_c__InverseKinematic_Request_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "robot_interfaces/srv/detail/inverse_kinematic__rosidl_typesupport_introspection_c.h"
// already included above
// #include "robot_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "robot_interfaces/srv/detail/inverse_kinematic__functions.h"
// already included above
// #include "robot_interfaces/srv/detail/inverse_kinematic__struct.h"


// Include directives for member types
// Member `message`
#include "rosidl_runtime_c/string_functions.h"
// Member `solution`
#include "rosidl_runtime_c/primitives_sequence_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void robot_interfaces__srv__InverseKinematic_Response__rosidl_typesupport_introspection_c__InverseKinematic_Response_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  robot_interfaces__srv__InverseKinematic_Response__init(message_memory);
}

void robot_interfaces__srv__InverseKinematic_Response__rosidl_typesupport_introspection_c__InverseKinematic_Response_fini_function(void * message_memory)
{
  robot_interfaces__srv__InverseKinematic_Response__fini(message_memory);
}

size_t robot_interfaces__srv__InverseKinematic_Response__rosidl_typesupport_introspection_c__size_function__InverseKinematic_Response__solution(
  const void * untyped_member)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return member->size;
}

const void * robot_interfaces__srv__InverseKinematic_Response__rosidl_typesupport_introspection_c__get_const_function__InverseKinematic_Response__solution(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void * robot_interfaces__srv__InverseKinematic_Response__rosidl_typesupport_introspection_c__get_function__InverseKinematic_Response__solution(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void robot_interfaces__srv__InverseKinematic_Response__rosidl_typesupport_introspection_c__fetch_function__InverseKinematic_Response__solution(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const double * item =
    ((const double *)
    robot_interfaces__srv__InverseKinematic_Response__rosidl_typesupport_introspection_c__get_const_function__InverseKinematic_Response__solution(untyped_member, index));
  double * value =
    (double *)(untyped_value);
  *value = *item;
}

void robot_interfaces__srv__InverseKinematic_Response__rosidl_typesupport_introspection_c__assign_function__InverseKinematic_Response__solution(
  void * untyped_member, size_t index, const void * untyped_value)
{
  double * item =
    ((double *)
    robot_interfaces__srv__InverseKinematic_Response__rosidl_typesupport_introspection_c__get_function__InverseKinematic_Response__solution(untyped_member, index));
  const double * value =
    (const double *)(untyped_value);
  *item = *value;
}

bool robot_interfaces__srv__InverseKinematic_Response__rosidl_typesupport_introspection_c__resize_function__InverseKinematic_Response__solution(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  rosidl_runtime_c__double__Sequence__fini(member);
  return rosidl_runtime_c__double__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember robot_interfaces__srv__InverseKinematic_Response__rosidl_typesupport_introspection_c__InverseKinematic_Response_message_member_array[3] = {
  {
    "success",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(robot_interfaces__srv__InverseKinematic_Response, success),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "message",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(robot_interfaces__srv__InverseKinematic_Response, message),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "solution",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(robot_interfaces__srv__InverseKinematic_Response, solution),  // bytes offset in struct
    NULL,  // default value
    robot_interfaces__srv__InverseKinematic_Response__rosidl_typesupport_introspection_c__size_function__InverseKinematic_Response__solution,  // size() function pointer
    robot_interfaces__srv__InverseKinematic_Response__rosidl_typesupport_introspection_c__get_const_function__InverseKinematic_Response__solution,  // get_const(index) function pointer
    robot_interfaces__srv__InverseKinematic_Response__rosidl_typesupport_introspection_c__get_function__InverseKinematic_Response__solution,  // get(index) function pointer
    robot_interfaces__srv__InverseKinematic_Response__rosidl_typesupport_introspection_c__fetch_function__InverseKinematic_Response__solution,  // fetch(index, &value) function pointer
    robot_interfaces__srv__InverseKinematic_Response__rosidl_typesupport_introspection_c__assign_function__InverseKinematic_Response__solution,  // assign(index, value) function pointer
    robot_interfaces__srv__InverseKinematic_Response__rosidl_typesupport_introspection_c__resize_function__InverseKinematic_Response__solution  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers robot_interfaces__srv__InverseKinematic_Response__rosidl_typesupport_introspection_c__InverseKinematic_Response_message_members = {
  "robot_interfaces__srv",  // message namespace
  "InverseKinematic_Response",  // message name
  3,  // number of fields
  sizeof(robot_interfaces__srv__InverseKinematic_Response),
  robot_interfaces__srv__InverseKinematic_Response__rosidl_typesupport_introspection_c__InverseKinematic_Response_message_member_array,  // message members
  robot_interfaces__srv__InverseKinematic_Response__rosidl_typesupport_introspection_c__InverseKinematic_Response_init_function,  // function to initialize message memory (memory has to be allocated)
  robot_interfaces__srv__InverseKinematic_Response__rosidl_typesupport_introspection_c__InverseKinematic_Response_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t robot_interfaces__srv__InverseKinematic_Response__rosidl_typesupport_introspection_c__InverseKinematic_Response_message_type_support_handle = {
  0,
  &robot_interfaces__srv__InverseKinematic_Response__rosidl_typesupport_introspection_c__InverseKinematic_Response_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_robot_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, robot_interfaces, srv, InverseKinematic_Response)() {
  if (!robot_interfaces__srv__InverseKinematic_Response__rosidl_typesupport_introspection_c__InverseKinematic_Response_message_type_support_handle.typesupport_identifier) {
    robot_interfaces__srv__InverseKinematic_Response__rosidl_typesupport_introspection_c__InverseKinematic_Response_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &robot_interfaces__srv__InverseKinematic_Response__rosidl_typesupport_introspection_c__InverseKinematic_Response_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "robot_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "robot_interfaces/srv/detail/inverse_kinematic__rosidl_typesupport_introspection_c.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/service_introspection.h"

// this is intentionally not const to allow initialization later to prevent an initialization race
static rosidl_typesupport_introspection_c__ServiceMembers robot_interfaces__srv__detail__inverse_kinematic__rosidl_typesupport_introspection_c__InverseKinematic_service_members = {
  "robot_interfaces__srv",  // service namespace
  "InverseKinematic",  // service name
  // these two fields are initialized below on the first access
  NULL,  // request message
  // robot_interfaces__srv__detail__inverse_kinematic__rosidl_typesupport_introspection_c__InverseKinematic_Request_message_type_support_handle,
  NULL  // response message
  // robot_interfaces__srv__detail__inverse_kinematic__rosidl_typesupport_introspection_c__InverseKinematic_Response_message_type_support_handle
};

static rosidl_service_type_support_t robot_interfaces__srv__detail__inverse_kinematic__rosidl_typesupport_introspection_c__InverseKinematic_service_type_support_handle = {
  0,
  &robot_interfaces__srv__detail__inverse_kinematic__rosidl_typesupport_introspection_c__InverseKinematic_service_members,
  get_service_typesupport_handle_function,
};

// Forward declaration of request/response type support functions
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, robot_interfaces, srv, InverseKinematic_Request)();

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, robot_interfaces, srv, InverseKinematic_Response)();

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_robot_interfaces
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, robot_interfaces, srv, InverseKinematic)() {
  if (!robot_interfaces__srv__detail__inverse_kinematic__rosidl_typesupport_introspection_c__InverseKinematic_service_type_support_handle.typesupport_identifier) {
    robot_interfaces__srv__detail__inverse_kinematic__rosidl_typesupport_introspection_c__InverseKinematic_service_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  rosidl_typesupport_introspection_c__ServiceMembers * service_members =
    (rosidl_typesupport_introspection_c__ServiceMembers *)robot_interfaces__srv__detail__inverse_kinematic__rosidl_typesupport_introspection_c__InverseKinematic_service_type_support_handle.data;

  if (!service_members->request_members_) {
    service_members->request_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, robot_interfaces, srv, InverseKinematic_Request)()->data;
  }
  if (!service_members->response_members_) {
    service_members->response_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, robot_interfaces, srv, InverseKinematic_Response)()->data;
  }

  return &robot_interfaces__srv__detail__inverse_kinematic__rosidl_typesupport_introspection_c__InverseKinematic_service_type_support_handle;
}
