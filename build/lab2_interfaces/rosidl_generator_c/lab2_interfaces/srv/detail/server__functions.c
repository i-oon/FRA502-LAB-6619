// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from lab2_interfaces:srv/Server.idl
// generated code does not contain a copyright notice
#include "lab2_interfaces/srv/detail/server__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"

// Include directives for member types
// Member `target`
#include "geometry_msgs/msg/detail/point__functions.h"

bool
lab2_interfaces__srv__Server_Request__init(lab2_interfaces__srv__Server_Request * msg)
{
  if (!msg) {
    return false;
  }
  // target
  if (!geometry_msgs__msg__Point__init(&msg->target)) {
    lab2_interfaces__srv__Server_Request__fini(msg);
    return false;
  }
  return true;
}

void
lab2_interfaces__srv__Server_Request__fini(lab2_interfaces__srv__Server_Request * msg)
{
  if (!msg) {
    return;
  }
  // target
  geometry_msgs__msg__Point__fini(&msg->target);
}

bool
lab2_interfaces__srv__Server_Request__are_equal(const lab2_interfaces__srv__Server_Request * lhs, const lab2_interfaces__srv__Server_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // target
  if (!geometry_msgs__msg__Point__are_equal(
      &(lhs->target), &(rhs->target)))
  {
    return false;
  }
  return true;
}

bool
lab2_interfaces__srv__Server_Request__copy(
  const lab2_interfaces__srv__Server_Request * input,
  lab2_interfaces__srv__Server_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // target
  if (!geometry_msgs__msg__Point__copy(
      &(input->target), &(output->target)))
  {
    return false;
  }
  return true;
}

lab2_interfaces__srv__Server_Request *
lab2_interfaces__srv__Server_Request__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  lab2_interfaces__srv__Server_Request * msg = (lab2_interfaces__srv__Server_Request *)allocator.allocate(sizeof(lab2_interfaces__srv__Server_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(lab2_interfaces__srv__Server_Request));
  bool success = lab2_interfaces__srv__Server_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
lab2_interfaces__srv__Server_Request__destroy(lab2_interfaces__srv__Server_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    lab2_interfaces__srv__Server_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
lab2_interfaces__srv__Server_Request__Sequence__init(lab2_interfaces__srv__Server_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  lab2_interfaces__srv__Server_Request * data = NULL;

  if (size) {
    data = (lab2_interfaces__srv__Server_Request *)allocator.zero_allocate(size, sizeof(lab2_interfaces__srv__Server_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = lab2_interfaces__srv__Server_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        lab2_interfaces__srv__Server_Request__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
lab2_interfaces__srv__Server_Request__Sequence__fini(lab2_interfaces__srv__Server_Request__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      lab2_interfaces__srv__Server_Request__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

lab2_interfaces__srv__Server_Request__Sequence *
lab2_interfaces__srv__Server_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  lab2_interfaces__srv__Server_Request__Sequence * array = (lab2_interfaces__srv__Server_Request__Sequence *)allocator.allocate(sizeof(lab2_interfaces__srv__Server_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = lab2_interfaces__srv__Server_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
lab2_interfaces__srv__Server_Request__Sequence__destroy(lab2_interfaces__srv__Server_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    lab2_interfaces__srv__Server_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
lab2_interfaces__srv__Server_Request__Sequence__are_equal(const lab2_interfaces__srv__Server_Request__Sequence * lhs, const lab2_interfaces__srv__Server_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!lab2_interfaces__srv__Server_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
lab2_interfaces__srv__Server_Request__Sequence__copy(
  const lab2_interfaces__srv__Server_Request__Sequence * input,
  lab2_interfaces__srv__Server_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(lab2_interfaces__srv__Server_Request);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    lab2_interfaces__srv__Server_Request * data =
      (lab2_interfaces__srv__Server_Request *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!lab2_interfaces__srv__Server_Request__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          lab2_interfaces__srv__Server_Request__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!lab2_interfaces__srv__Server_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


bool
lab2_interfaces__srv__Server_Response__init(lab2_interfaces__srv__Server_Response * msg)
{
  if (!msg) {
    return false;
  }
  // structure_needs_at_least_one_member
  return true;
}

void
lab2_interfaces__srv__Server_Response__fini(lab2_interfaces__srv__Server_Response * msg)
{
  if (!msg) {
    return;
  }
  // structure_needs_at_least_one_member
}

bool
lab2_interfaces__srv__Server_Response__are_equal(const lab2_interfaces__srv__Server_Response * lhs, const lab2_interfaces__srv__Server_Response * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // structure_needs_at_least_one_member
  if (lhs->structure_needs_at_least_one_member != rhs->structure_needs_at_least_one_member) {
    return false;
  }
  return true;
}

bool
lab2_interfaces__srv__Server_Response__copy(
  const lab2_interfaces__srv__Server_Response * input,
  lab2_interfaces__srv__Server_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // structure_needs_at_least_one_member
  output->structure_needs_at_least_one_member = input->structure_needs_at_least_one_member;
  return true;
}

lab2_interfaces__srv__Server_Response *
lab2_interfaces__srv__Server_Response__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  lab2_interfaces__srv__Server_Response * msg = (lab2_interfaces__srv__Server_Response *)allocator.allocate(sizeof(lab2_interfaces__srv__Server_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(lab2_interfaces__srv__Server_Response));
  bool success = lab2_interfaces__srv__Server_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
lab2_interfaces__srv__Server_Response__destroy(lab2_interfaces__srv__Server_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    lab2_interfaces__srv__Server_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
lab2_interfaces__srv__Server_Response__Sequence__init(lab2_interfaces__srv__Server_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  lab2_interfaces__srv__Server_Response * data = NULL;

  if (size) {
    data = (lab2_interfaces__srv__Server_Response *)allocator.zero_allocate(size, sizeof(lab2_interfaces__srv__Server_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = lab2_interfaces__srv__Server_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        lab2_interfaces__srv__Server_Response__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
lab2_interfaces__srv__Server_Response__Sequence__fini(lab2_interfaces__srv__Server_Response__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      lab2_interfaces__srv__Server_Response__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

lab2_interfaces__srv__Server_Response__Sequence *
lab2_interfaces__srv__Server_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  lab2_interfaces__srv__Server_Response__Sequence * array = (lab2_interfaces__srv__Server_Response__Sequence *)allocator.allocate(sizeof(lab2_interfaces__srv__Server_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = lab2_interfaces__srv__Server_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
lab2_interfaces__srv__Server_Response__Sequence__destroy(lab2_interfaces__srv__Server_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    lab2_interfaces__srv__Server_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
lab2_interfaces__srv__Server_Response__Sequence__are_equal(const lab2_interfaces__srv__Server_Response__Sequence * lhs, const lab2_interfaces__srv__Server_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!lab2_interfaces__srv__Server_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
lab2_interfaces__srv__Server_Response__Sequence__copy(
  const lab2_interfaces__srv__Server_Response__Sequence * input,
  lab2_interfaces__srv__Server_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(lab2_interfaces__srv__Server_Response);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    lab2_interfaces__srv__Server_Response * data =
      (lab2_interfaces__srv__Server_Response *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!lab2_interfaces__srv__Server_Response__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          lab2_interfaces__srv__Server_Response__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!lab2_interfaces__srv__Server_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
