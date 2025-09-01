// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from lab2_interfaces:srv/Server.idl
// generated code does not contain a copyright notice

#ifndef LAB2_INTERFACES__SRV__DETAIL__SERVER__STRUCT_HPP_
#define LAB2_INTERFACES__SRV__DETAIL__SERVER__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'target'
#include "geometry_msgs/msg/detail/point__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__lab2_interfaces__srv__Server_Request __attribute__((deprecated))
#else
# define DEPRECATED__lab2_interfaces__srv__Server_Request __declspec(deprecated)
#endif

namespace lab2_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct Server_Request_
{
  using Type = Server_Request_<ContainerAllocator>;

  explicit Server_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : target(_init)
  {
    (void)_init;
  }

  explicit Server_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : target(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _target_type =
    geometry_msgs::msg::Point_<ContainerAllocator>;
  _target_type target;

  // setters for named parameter idiom
  Type & set__target(
    const geometry_msgs::msg::Point_<ContainerAllocator> & _arg)
  {
    this->target = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    lab2_interfaces::srv::Server_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const lab2_interfaces::srv::Server_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<lab2_interfaces::srv::Server_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<lab2_interfaces::srv::Server_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      lab2_interfaces::srv::Server_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<lab2_interfaces::srv::Server_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      lab2_interfaces::srv::Server_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<lab2_interfaces::srv::Server_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<lab2_interfaces::srv::Server_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<lab2_interfaces::srv::Server_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__lab2_interfaces__srv__Server_Request
    std::shared_ptr<lab2_interfaces::srv::Server_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__lab2_interfaces__srv__Server_Request
    std::shared_ptr<lab2_interfaces::srv::Server_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Server_Request_ & other) const
  {
    if (this->target != other.target) {
      return false;
    }
    return true;
  }
  bool operator!=(const Server_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Server_Request_

// alias to use template instance with default allocator
using Server_Request =
  lab2_interfaces::srv::Server_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace lab2_interfaces


#ifndef _WIN32
# define DEPRECATED__lab2_interfaces__srv__Server_Response __attribute__((deprecated))
#else
# define DEPRECATED__lab2_interfaces__srv__Server_Response __declspec(deprecated)
#endif

namespace lab2_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct Server_Response_
{
  using Type = Server_Response_<ContainerAllocator>;

  explicit Server_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->structure_needs_at_least_one_member = 0;
    }
  }

  explicit Server_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->structure_needs_at_least_one_member = 0;
    }
  }

  // field types and members
  using _structure_needs_at_least_one_member_type =
    uint8_t;
  _structure_needs_at_least_one_member_type structure_needs_at_least_one_member;


  // constant declarations

  // pointer types
  using RawPtr =
    lab2_interfaces::srv::Server_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const lab2_interfaces::srv::Server_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<lab2_interfaces::srv::Server_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<lab2_interfaces::srv::Server_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      lab2_interfaces::srv::Server_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<lab2_interfaces::srv::Server_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      lab2_interfaces::srv::Server_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<lab2_interfaces::srv::Server_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<lab2_interfaces::srv::Server_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<lab2_interfaces::srv::Server_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__lab2_interfaces__srv__Server_Response
    std::shared_ptr<lab2_interfaces::srv::Server_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__lab2_interfaces__srv__Server_Response
    std::shared_ptr<lab2_interfaces::srv::Server_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Server_Response_ & other) const
  {
    if (this->structure_needs_at_least_one_member != other.structure_needs_at_least_one_member) {
      return false;
    }
    return true;
  }
  bool operator!=(const Server_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Server_Response_

// alias to use template instance with default allocator
using Server_Response =
  lab2_interfaces::srv::Server_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace lab2_interfaces

namespace lab2_interfaces
{

namespace srv
{

struct Server
{
  using Request = lab2_interfaces::srv::Server_Request;
  using Response = lab2_interfaces::srv::Server_Response;
};

}  // namespace srv

}  // namespace lab2_interfaces

#endif  // LAB2_INTERFACES__SRV__DETAIL__SERVER__STRUCT_HPP_
