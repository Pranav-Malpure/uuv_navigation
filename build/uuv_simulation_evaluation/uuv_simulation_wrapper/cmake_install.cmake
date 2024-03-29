# Install script for directory: /home/pranavmalpure/uuv_simulator_orig/src/uuv_simulation_evaluation/uuv_simulation_wrapper

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/pranavmalpure/uuv_simulator_orig/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  include("/home/pranavmalpure/uuv_simulator_orig/build/uuv_simulation_evaluation/uuv_simulation_wrapper/catkin_generated/safe_execute_install.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/pranavmalpure/uuv_simulator_orig/build/uuv_simulation_evaluation/uuv_simulation_wrapper/catkin_generated/installspace/uuv_simulation_wrapper.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/uuv_simulation_wrapper/cmake" TYPE FILE FILES
    "/home/pranavmalpure/uuv_simulator_orig/build/uuv_simulation_evaluation/uuv_simulation_wrapper/catkin_generated/installspace/uuv_simulation_wrapperConfig.cmake"
    "/home/pranavmalpure/uuv_simulator_orig/build/uuv_simulation_evaluation/uuv_simulation_wrapper/catkin_generated/installspace/uuv_simulation_wrapperConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/uuv_simulation_wrapper" TYPE FILE FILES "/home/pranavmalpure/uuv_simulator_orig/src/uuv_simulation_evaluation/uuv_simulation_wrapper/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/uuv_simulation_wrapper" TYPE PROGRAM FILES "/home/pranavmalpure/uuv_simulator_orig/build/uuv_simulation_evaluation/uuv_simulation_wrapper/catkin_generated/installspace/set_simulation_timer")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/uuv_simulation_wrapper" TYPE PROGRAM FILES "/home/pranavmalpure/uuv_simulator_orig/build/uuv_simulation_evaluation/uuv_simulation_wrapper/catkin_generated/installspace/unpause_simulation")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/uuv_simulation_wrapper" TYPE DIRECTORY FILES "/home/pranavmalpure/uuv_simulator_orig/src/uuv_simulation_evaluation/uuv_simulation_wrapper/launch" REGEX "/[^/]*\\~$" EXCLUDE)
endif()

