# Install script for directory: /home/pranavmalpure/uuv_simulator_orig/src/uuv_simulation_evaluation/uuv_smac_utils

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
  include("/home/pranavmalpure/uuv_simulator_orig/build/uuv_simulation_evaluation/uuv_smac_utils/catkin_generated/safe_execute_install.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/pranavmalpure/uuv_simulator_orig/build/uuv_simulation_evaluation/uuv_smac_utils/catkin_generated/installspace/uuv_smac_utils.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/uuv_smac_utils/cmake" TYPE FILE FILES
    "/home/pranavmalpure/uuv_simulator_orig/build/uuv_simulation_evaluation/uuv_smac_utils/catkin_generated/installspace/uuv_smac_utilsConfig.cmake"
    "/home/pranavmalpure/uuv_simulator_orig/build/uuv_simulation_evaluation/uuv_smac_utils/catkin_generated/installspace/uuv_smac_utilsConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/uuv_smac_utils" TYPE FILE FILES "/home/pranavmalpure/uuv_simulator_orig/src/uuv_simulation_evaluation/uuv_smac_utils/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/uuv_smac_utils" TYPE PROGRAM FILES "/home/pranavmalpure/uuv_simulator_orig/build/uuv_simulation_evaluation/uuv_smac_utils/catkin_generated/installspace/smac_wrapper")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/uuv_smac_utils" TYPE PROGRAM FILES "/home/pranavmalpure/uuv_simulator_orig/build/uuv_simulation_evaluation/uuv_smac_utils/catkin_generated/installspace/run_smac")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/uuv_smac_utils" TYPE PROGRAM FILES "/home/pranavmalpure/uuv_simulator_orig/build/uuv_simulation_evaluation/uuv_smac_utils/catkin_generated/installspace/create_smac_config_files")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/uuv_smac_utils" TYPE PROGRAM FILES "/home/pranavmalpure/uuv_simulator_orig/build/uuv_simulation_evaluation/uuv_smac_utils/catkin_generated/installspace/evaluate_smac_best_results")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/uuv_smac_utils" TYPE PROGRAM FILES "/home/pranavmalpure/uuv_simulator_orig/build/uuv_simulation_evaluation/uuv_smac_utils/catkin_generated/installspace/smac")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/uuv_smac_utils" TYPE PROGRAM FILES "/home/pranavmalpure/uuv_simulator_orig/build/uuv_simulation_evaluation/uuv_smac_utils/catkin_generated/installspace/create_results_folder")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/uuv_smac_utils" TYPE PROGRAM FILES "/home/pranavmalpure/uuv_simulator_orig/build/uuv_simulation_evaluation/uuv_smac_utils/catkin_generated/installspace/generate_motion_primitives")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/uuv_smac_utils" TYPE PROGRAM FILES "/home/pranavmalpure/uuv_simulator_orig/build/uuv_simulation_evaluation/uuv_smac_utils/catkin_generated/installspace/sync_smac_files")
endif()

