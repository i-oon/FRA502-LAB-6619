// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from lab2_interfaces:srv/Server.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "lab2_interfaces/srv/detail/server__rosidl_typesupport_introspection_c.h"
#include "lab2_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "lab2_interfaces/srv/detail/server__functions.h"
#include "lab2_interfaces/srv/detail/server__struct.h"


// Include directives for member types
// Member `target`
#include "geometry_msgs/msg/point.h"
// Member `target`
#include "geometry_msgs/msg/detail/point__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void lab2_interfaces__srv__Server_Request__rosidl_typesupport_introspection_c__Server_Request_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  lab2_interfaces__srv__Server_Request__init(message_memory);
}

void lab2_interfaces__srv__Server_Request__rosidl_typesupport_introspection_c__Server_Request_fini_function(void * message_memory)
{
  lab2_interfaces__srv__Server_Request__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember lab2_interfaces__srv__Server_Request__rosidl_typesupport_introspection_c__Server_Request_message_member_array[1] = {
  {
    "target",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(lab2_interfaces__srv__Server_Request, target),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers lab2_interfaces__srv__Server_Request__rosidl_typesupport_introspection_c__Server_Request_message_members = {
  "lab2_interfaces__srv",  // message namespace
  "Server_Request",  // message name
  1,  // number of fields
  sizeof(lab2_interfaces__srv__Server_Request),
  lab2_interfaces__srv__Server_Request__rosidl_typesupport_introspection_c__Server_Request_message_member_array,  // message members
  lab2_interfaces__srv__Server_Request__rosidl_typesupport_introspection_c__Server_Request_init_function,  // function to initialize message memory (memory has to be allocated)
  lab2_interfaces__srv__Server_Request__rosidl_typesupport_introspection_c__Server_Request_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t lab2_interfaces__srv__Server_Request__rosidl_typesupport_introspection_c__Server_Request_message_type_support_handle = {
  0,
  &lab2_interfaces__srv__Server_Request__rosidl_typesupport_introspection_c__Server_Request_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_lab2_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, lab2_interfaces, srv, Server_Request)() {
  lab2_interfaces__srv__Server_Request__rosidl_typesupport_introspection_c__Server_Request_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, geometry_msgs, msg, Point)();
  if (!lab2_interfaces__srv__Server_Request__rosidl_typesupport_introspection_c__Server_Request_message_type_support_handle.typesupport_identifier) {
    lab2_interfaces__srv__Server_Request__rosidl_typesupport_introspection_c__Server_Request_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &lab2_interfaces__srv__Server_Request__rosidl_typesupport_introspection_c__Server_Request_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "lab2_interfaces/srv/detail/server__rosidl_typesupport_introspection_c.h"
// already included above
// #include "lab2_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "lab2_interfaces/srv/detail/server__functions.h"
// already included above
// #include "lab2_interfaces/srv/detail/server__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void lab2_interfaces__srv__Server_Response__rosidl_typesupport_introspection_c__Server_Response_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  lab2_interfaces__srv__Server_Response__init(message_memory);
}

void lab2_interfaces__srv__Server_Response__rosidl_typesupport_introspection_c__Server_Response_fini_function(void * message_memory)
{
  lab2_interfaces__srv__Server_Response__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember lab2_interfaces__srv__Server_Response__rosidl_typesupport_introspection_c__Server_Response_message_member_array[1] = {
  {
    "structure_needs_at_least_one_member",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(lab2_interfaces__srv__Server_Response, structure_needs_at_least_one_member),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers lab2_interfaces__srv__Server_Response__rosidl_typesupport_introspection_c__Server_Response_message_members = {
  "lab2_interfaces__srv",  // message namespace
  "Server_Response",  // message name
  1,  // number of fields
  sizeof(lab2_interfaces__srv__Server_Response),
  lab2_interfaces__srv__Server_Response__rosidl_typesupport_introspection_c__Server_Response_message_member_array,  // message members
  lab2_interfaces__srv__Server_Response__rosidl_typesupport_introspection_c__Server_Response_init_function,  // function to initialize message memory (memory has to be allocated)
  lab2_interfaces__srv__Server_Response__rosidl_typesupport_introspection_c__Server_Response_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t lab2_interfaces__srv__Server_Response__rosidl_typesupport_introspection_c__Server_Response_message_type_support_handle = {
  0,
  &lab2_interfaces__srv__Server_Response__rosidl_typesupport_introspection_c__Server_Response_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_lab2_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, lab2_interfaces, srv, Server_Response)() {
  if (!lab2_interfaces__srv__Server_Response__rosidl_typesupport_introspection_c__Server_Response_message_type_support_handle.typesupport_identifier) {
    lab2_interfaces__srv__Server_Response__rosidl_typesupport_introspection_c__Server_Response_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &lab2_interfaces__srv__Server_Response__rosidl_typesupport_introspection_c__Server_Response_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "lab2_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "lab2_interfaces/srv/detail/server__rosidl_typesupport_introspection_c.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/service_introspection.h"

// this is intentionally not const to allow initialization later to prevent an initialization race
static rosidl_typesupport_introspection_c__ServiceMembers lab2_interfaces__srv__detail__server__rosidl_typesupport_introspection_c__Server_service_members = {
  "lab2_interfaces__srv",  // service namespace
  "Server",  // service name
  // these two fields are initialized below on the first access
  NULL,  // request message
  // lab2_interfaces__srv__detail__server__rosidl_typesupport_introspection_c__Server_Request_message_type_support_handle,
  NULL  // response message
  // lab2_interfaces__srv__detail__server__rosidl_typesupport_introspection_c__Server_Response_message_type_support_handle
};

static rosidl_service_type_support_t lab2_interfaces__srv__detail__server__rosidl_typesupport_introspection_c__Server_service_type_support_handle = {
  0,
  &lab2_interfaces__srv__detail__server__rosidl_typesupport_introspection_c__Server_service_members,
  get_service_typesupport_handle_function,
};

// Forward declaration of request/response type support functions
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, lab2_interfaces, srv, Server_Request)();

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, lab2_interfaces, srv, Server_Response)();

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_lab2_interfaces
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, lab2_interfaces, srv, Server)() {
  if (!lab2_interfaces__srv__detail__server__rosidl_typesupport_introspection_c__Server_service_type_support_handle.typesupport_identifier) {
    lab2_interfaces__srv__detail__server__rosidl_typesupport_introspection_c__Server_service_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  rosidl_typesupport_introspection_c__ServiceMembers * service_members =
    (rosidl_typesupport_introspection_c__ServiceMembers *)lab2_interfaces__srv__detail__server__rosidl_typesupport_introspection_c__Server_service_type_support_handle.data;

  if (!service_members->request_members_) {
    service_members->request_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, lab2_interfaces, srv, Server_Request)()->data;
  }
  if (!service_members->response_members_) {
    service_members->response_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, lab2_interfaces, srv, Server_Response)()->data;
  }

  return &lab2_interfaces__srv__detail__server__rosidl_typesupport_introspection_c__Server_service_type_support_handle;
}
