# ROS Workspace Analysis Report
Generated on: 2025-01-19 11:49:36
Workspace Path: ~/amr_ws

## Project Structure
### Directory Tree
```
- amr_ws/
  - src/
    - amr_controller/
      - CMakeLists.txt
      - package.xml
      - include/
        - amr_controller/
      - launch/
      - scripts/
      - src/
    - amr_description/
      - CMakeLists.txt
      - package.xml
      - config/
        - rviz/
      - launch/
      - meshes/
      - urdf/
    - amr_imu_filters/
      - CMakeLists.txt
      - package.xml
      - cfg/
      - include/
        - amr_imu_filters/
      - launch/
      - src/
    - amr_laser_filters/
      - CMakeLists.txt
      - package.xml
      - config/
      - include/
        - amr_laser_filters/
      - launch/
      - src/
    - amr_launcher/
      - CMakeLists.txt
      - package.xml
      - config/
        - debug/
        - laser/
        - navi/
          - base_mit/
          - sanden/
          - smts/
        - rviz/
        - slam/
      - data/
        - graphs/
        - navi_data/
      - include/
        - amr_launcher/
      - launch/
        - debug/
        - hard_bridge/
        - map/
        - navigation/
        - robot/
        - sensor_data/
        - slam/
        - slam_navi/
      - maps/
      - prohibition_areas/
      - scripts/
      - src/
      - waypoints/
    - amr_lidar_localization/
      - CMakeLists.txt
      - package.xml
      - include/
        - amr_lidar_localization/
      - launch/
      - src/
    - amr_map/
      - CMakeLists.txt
      - package.xml
      - include/
        - map_pkg/
      - launch/
      - scripts/
      - src/
    - amr_monitor/
      - CMakeLists.txt
      - package.xml
      - config/
        - topics/
      - data/
      - include/
        - amr_monitor/
      - launch/
      - resources/
        - icons/
        - themes/
        - ui/
          - monitors/
      - scripts/
      - src/
        - amr_monitor/
          - monitors/
          - ui/
          - __pycache__/
    - amr_navi/
      - CMakeLists.txt
      - package.xml
      - config/
        - navi/
        - rviz/
      - include/
        - nav_pkg/
      - launch/
      - scripts/
      - src/
    - amr_nova/
      - CMakeLists.txt
      - package.xml
      - config/
      - data/
      - include/
        - amr_nova/
      - launch/
      - maps/
      - msg/
      - resources/
        - icons/
        - images/
      - rviz/
      - scripts/
      - src/
        - cpp/
        - python/
      - srv/
      - ui/
      - waypoints/
    - amr_slam/
      - CMakeLists.txt
      - package.xml
      - config/
        - rviz/
      - include/
        - slam_pkg/
      - launch/
      - map/
      - scripts/
      - src/
    - amr_waypoint_tools/
      - CMakeLists.txt
      - package.xml
      - doc/
      - icons/
        - classes/
      - include/
      - launch/
      - media/
      - meshes/
      - msg/
      - rviz/
      - scripts/
      - src/
        - network/
      - srv/
    - audio_compass/
      - CMakeLists.txt
      - package.xml
      - config/
      - include/
        - audio_compass/
      - launch/
      - models/
      - msg/
      - scripts/
        - test/
      - src/
        - speech_generator/
        - speech_recognizer/
      - srv/
    - direction_indicator/
      - CMakeLists.txt
      - package.xml
      - config/
      - include/
        - direction_indicator/
      - launch/
      - scripts/
      - src/
    - hoshi_planner/
      - CMakeLists.txt
      - package.xml
      - include/
        - hoshi_planner/
      - src/
    - jie_ware/
      - CMakeLists.txt
      - package.xml
      - launch/
      - src/
    - om_modbus_master/
      - CMakeLists.txt
      - package.xml
      - include/
        - om_modbus_master/
      - launch/
      - msg/
      - sample/
        - cpp/
          - AZ/
          - BLV/
          - MobiCon/
        - python/
          - AZ/
          - BLV/
          - BLV-R/
          - MobiCon/
      - scripts/
      - src/
    - prohibition_areas_plugin/
      - CMakeLists.txt
      - package.xml
      - config/
      - icons/
      - include/
        - prohibition_areas_plugin/
          - prohibition_areas_layer/
          - prohibition_areas_tool/
      - launch/
      - maps/
      - msg/
      - prohibition_areas/
      - resources/
      - rviz/
      - src/
        - prohibition_areas_layer/
        - prohibition_areas_tool/
    - rplidar_ros/
      - CMakeLists.txt
      - package.xml
      - debian/
      - launch/
      - rviz/
      - scripts/
      - sdk/
        - include/
        - src/
          - arch/
          - dataunpacker/
          - hal/
      - src/
    - wp_nav_controller/
      - CMakeLists.txt
      - package.xml
      - doc/
      - include/
        - wp_nav_controller/
      - launch/
      - msg/
      - rviz/
      - scripts/
      - src/
        - wp_nav_controller/
          - gui/
      - srv/
```

## Build System

## Package Analysis

Found 20 packages:

### Package: amr_controller

#### Dependencies (package.xml)

- build_depends:
  - geometry_msgs
  - roscpp
  - rospy
  - sensor_msgs

- exec_depends:
  - geometry_msgs
  - roscpp
  - rospy
  - sensor_msgs

#### CMake Dependencies

- find_package:
  - Boost
  - catkin

#### Launch Files
- launch\amr_controller.launch

### Package: amr_description

#### Dependencies (package.xml)

- build_depends:
  - robot_state_publisher
  - urdf
  - xacro

- exec_depends:
  - robot_state_publisher
  - urdf
  - xacro

#### CMake Dependencies

- find_package:
  - Boost
  - catkin

#### Launch Files
- launch\amr_description.launch
- launch\amr_description_view.launch

### Package: amr_imu_filters

#### Dependencies (package.xml)

- build_depends:
  - message_generation

- exec_depends:
  - message_runtime

#### CMake Dependencies

- find_package:
  - Boost
  - Eigen3
  - catkin

#### Launch Files
- launch\amr_advanced_imu_filter.launch
- launch\amr_imu_filter.launch

### Package: amr_laser_filters

#### Dependencies (package.xml)

- build_depends:
  - roscpp
  - rospy
  - sensor_msgs

- exec_depends:
  - roscpp
  - rospy
  - sensor_msgs

#### CMake Dependencies

- find_package:
  - Boost
  - catkin

#### Launch Files
- launch\adaptive_laser_compressor.launch
- launch\laser_median_filter.launch
- launch\scan_filter.launch

### Package: amr_launcher

#### Dependencies (package.xml)

- build_depends:
  - geometry_msgs
  - nav_msgs
  - robot_state_publisher
  - roscpp
  - rospy
  - sensor_msgs
  - std_msgs
  - tf2
  - tf2_ros
  - xacro

- exec_depends:
  - PySide6
  - geometry_msgs
  - nav_msgs
  - robot_state_publisher
  - roscpp
  - rospy
  - sensor_msgs
  - std_msgs
  - tf2
  - tf2_ros
  - xacro

#### CMake Dependencies

- find_package:
  - Boost
  - catkin

#### Launch Files
- launch\amr_launch_navi.launch
- launch\amr_launch_navi_cartographer.launch
- launch\amr_launch_navi_gmapping.launch
- launch\amr_launch_navi_lidar_locator.launch
- launch\amr_launch_slam.launch
- launch\amr_launch_slam_cartographer.launch
- launch\debug\amr_description_view.launch
- launch\debug\amr_navi_recorder.launch
- launch\debug\amr_node_tf_generator.launch
- launch\debug\amr_rosbag.launch
- launch\debug\amr_rplidar_s2_view.launch
- launch\debug\amr_rqt_multiplot.launch
- launch\debug\amr_slam_recorder.launch
- launch\hard_bridge\amr_audio_ros_bridge.launch
- launch\hard_bridge\amr_controller.launch
- launch\hard_bridge\amr_mobi_con.launch
- launch\hard_bridge\amr_rplidar_s2.launch
- launch\hard_bridge\amr_speech_generator.launch
- launch\hard_bridge\amr_speech_recognizer.launch
- launch\map\amr_costmap_cleaner.launch
- launch\map\amr_map_pbstream2map.launch
- launch\map\amr_map_saver.launch
- launch\map\amr_map_saver_cartographer.launch
- launch\map\amr_prohibition_areas_editor.launch
- launch\map\amr_waypoint_add.launch
- launch\map\amr_waypoint_editor.launch
- launch\map\amr_waypoint_saver.launch
- launch\navigation\amr_amcl.launch
- launch\navigation\amr_direction_indicator.launch
- launch\navigation\amr_lidar_localization.launch
- launch\navigation\amr_map_server.launch
- launch\navigation\amr_move_base.launch
- launch\navigation\amr_navi_cartographer.launch
- launch\navigation\amr_navi_controller.launch
- launch\navigation\amr_navi_gmapping.launch
- launch\navigation\amr_waypoint.launch
- launch\navigation\amr_waypoint_go.launch
- launch\robot\amr_description.launch
- launch\sensor_data\amr_advanced_imu_filter.launch
- launch\sensor_data\amr_imu_filter.launch
- launch\sensor_data\amr_laser_filters.launch
- launch\slam\amr_slam_cartographer.launch
- launch\slam\amr_slam_gmapping.launch
- launch\slam\amr_slam_hector.launch
- launch\slam_navi\amr_sn_cartographer.launch
- launch\slam_navi\amr_sn_gmapping.launch

### Package: amr_lidar_localization

#### Dependencies (package.xml)

- build_depends:
  - cv_bridge
  - geometry_msgs
  - move_base_msgs
  - nav_msgs
  - roscpp
  - rospy
  - sensor_msgs
  - std_msgs
  - tf2
  - tf2_ros

- exec_depends:
  - cv_bridge
  - geometry_msgs
  - move_base_msgs
  - nav_msgs
  - roscpp
  - rospy
  - sensor_msgs
  - std_msgs
  - tf2
  - tf2_ros

#### CMake Dependencies

- find_package:
  - Boost
  - OpenCV
  - catkin

#### Launch Files
- launch\amcl_test.launch
- launch\lidar_loc_test.launch

### Package: amr_map

#### Dependencies (package.xml)

- build_depends:
  - geometry_msgs
  - move_base_msgs
  - nav_msgs
  - roscpp
  - rospy
  - sensor_msgs
  - std_msgs
  - tf2

- exec_depends:
  - geometry_msgs
  - move_base_msgs
  - nav_msgs
  - roscpp
  - rospy
  - sensor_msgs
  - std_msgs
  - tf2

#### CMake Dependencies

- find_package:
  - Boost
  - catkin

#### Launch Files
- launch\amr_map_saver.launch
- launch\amr_map_server.launch

### Package: amr_monitor

#### Dependencies (package.xml)

- build_depends:
  - dynamic_reconfigure
  - geometry_msgs
  - nav_msgs
  - roscpp
  - rospy
  - sensor_msgs
  - std_msgs
  - tf2
  - tf2_ros

- exec_depends:
  - dynamic_reconfigure
  - geometry_msgs
  - nav_msgs
  - python3-matplotlib
  - python3-numpy
  - python3-pandas
  - python3-psutil
  - python3-pyqtgraph
  - python3-pyside6
  - python3-pytest
  - python3-scipy
  - python3-yaml
  - roscpp
  - rospy
  - sensor_msgs
  - std_msgs
  - tf2
  - tf2_ros

#### CMake Dependencies

- find_package:
  - Boost
  - catkin

#### Launch Files
- launch\amr_monitor.launch

#### Installation Scripts

##### install.sh
```bash
#!/bin/bash

# 检查是否在工作空间中
if [ ! -f "src/amr_monitor/package.xml" ]; then
    echo "错误：请在catkin工作空间根目录运行此脚本"
    exit 1
fi

# 检查依赖
chmod +x src/amr_monitor/scripts/check_dependencies.sh
./src/amr_monitor/scripts/check_dependencies.sh
if [ $? -ne 0 ]; then
    echo "依赖检查失败，请先安装所需依赖"
    exit 1
fi

# 确保config目录存在
mkdir -p src/amr_monitor/config
mkdir -p src/amr_monitor/data

# 复制默认配置到配置文件
cp src/amr_monitor/config/default_config.yaml src/amr_monitor/config/config.yaml

# 编译功能包
catkin_make

source devel/setup.bash

# 设置执行权限
chmod +x src/amr_monitor/scripts/monitor_node.py

echo "安装完成！"

```

### Package: amr_navi

#### Dependencies (package.xml)

- build_depends:
  - actionlib
  - move_base_msgs
  - nav_msgs
  - roscpp
  - rospy
  - sensor_msgs
  - std_msgs
  - tf2_ros

- exec_depends:
  - actionlib
  - move_base_msgs
  - nav_msgs
  - roscpp
  - rospy
  - sensor_msgs
  - std_msgs
  - tf2_ros

#### CMake Dependencies

- find_package:
  - Boost
  - catkin

#### Launch Files
- launch\amr_navi.launch
- launch\demo_navi.launch

### Package: amr_nova

#### Dependencies (package.xml)

- build_depends:
  - actionlib
  - dynamic_reconfigure
  - geometry_msgs
  - move_base_msgs
  - nav_msgs
  - roscpp
  - rospy
  - sensor_msgs
  - std_msgs
  - tf2
  - tf2_ros

- exec_depends:
  - PySide6
  - actionlib
  - dynamic_reconfigure
  - geometry_msgs
  - move_base_msgs
  - nav_msgs
  - python3-pyside6
  - roscpp
  - rospy
  - sensor_msgs
  - std_msgs
  - tf2
  - tf2_ros

#### CMake Dependencies

- find_package:
  - Boost
  - Qt6
  - catkin

### Package: amr_slam

#### Dependencies (package.xml)

- build_depends:
  - nav_msgs
  - roscpp
  - rospy
  - sensor_msgs
  - std_msgs
  - tf2_ros

- exec_depends:
  - nav_msgs
  - roscpp
  - rospy
  - sensor_msgs
  - std_msgs
  - tf2_ros

#### CMake Dependencies

- find_package:
  - Boost
  - catkin

#### Launch Files
- launch\amr_cartographer.launch
- launch\amr_gmapping.launch
- launch\amr_hector.launch
- launch\gmapping.launch
- launch\hector.launch

### Package: amr_waypoint_tools

#### Dependencies (package.xml)

- build_depends:
  - actionlib
  - cmake_modules
  - geometry_msgs
  - interactive_markers
  - message_generation
  - roscpp
  - rviz
  - std_msgs
  - tf
  - tinyxml
  - visualization_msgs

- run_depends:
  - actionlib
  - geometry_msgs
  - interactive_markers
  - message_runtime
  - roscpp
  - rviz
  - std_msgs
  - tf
  - tinyxml
  - visualization_msgs

#### CMake Dependencies

- find_package:
  - Qt4
  - Qt5
  - TinyXML
  - catkin

#### Launch Files
- launch\add_waypoint.launch
- launch\add_waypoint_ai.launch
- launch\add_waypoint_app.launch
- launch\add_waypoint_mani.launch
- launch\add_waypoint_monitor.launch
- launch\add_waypoint_simulation.launch
- launch\add_waypoint_warehousing.launch
- launch\add_waypoint_wpr1.launch
- launch\add_waypoint_wpv3.launch
- launch\add_waypoint_wpv4.launch
- launch\wpb_ai_nav_test.launch
- launch\wpb_home_nav_remote.launch
- launch\wpb_home_nav_test.launch
- launch\wpb_mani_nav_test.launch
- launch\wpr1_nav_remote.launch
- launch\wpr1_nav_test.launch
- launch\wpv3_nav_test.launch

#### Installation Scripts

##### install_for_indigo.sh
```bash
#!/bin/bash
sudo apt-get update
sudo apt-get install ros-indigo-map-server
sudo apt-get install ros-indigo-navigation
```

##### install_for_kinetic.sh
```bash
#!/bin/bash
sudo apt-get update
sudo apt-get install ros-kinetic-map-server
sudo apt-get install ros-kinetic-navigation
```

##### install_for_melodic.sh
```bash
#!/bin/bash
sudo apt-get update
sudo apt-get install ros-melodic-map-server
sudo apt-get install ros-melodic-navigation
```

##### install_for_noetic.sh
```bash
#!/bin/bash
sudo apt-get update
sudo apt-get install ros-noetic-map-server
sudo apt-get install ros-noetic-navigation
```

### Package: audio_compass

#### Dependencies (package.xml)

- exec_depends:
  - message_runtime

#### CMake Dependencies

- find_package:
  - catkin

#### Launch Files
- launch\audio_ros_bridge.launch
- launch\speech_generator.launch
- launch\speech_recognizer.launch

#### Installation Scripts

##### install.sh
```bash
#!/bin/bash

# 设置颜色输出
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# 打印带颜色的消息
print_msg() {
    local color=$1
    local msg=$2
    echo -e "${color}${msg}${NC}"
}

# 检查命令是否存在
check_command() {
    if ! command -v $1 &> /dev/null; then
        return 1
    fi
    return 0
}

# 检查Python包是否已安装
check_python_package() {
    local package=$1
    local module=$1

    # 特殊包名与模块名的映射
    case $package in
        "SpeechRecognition")
            module="speech_recognition"
            ;;
        "openai-whisper")
            module="whisper"
            ;;
    esac

    # 优先检查 pip 安装状态
    if python3 -m pip show $package &> /dev/null; then
        return 0
    fi

    # 如果 pip 检查失败，再尝试直接导入模块检测
    if python3 -c "import $module" &> /dev/null; then
        return 0
    fi

    return 1
}

# 确保脚本以root权限运行
if [ "$EUID" -ne 0 ]; then
    print_msg $RED "请使用sudo运行此脚本"
    exit 1
fi

# 检查ROS环境
if ! check_command rosversion; then
    print_msg $RED "未检测到ROS环境，请先安装ROS并source环境"
    exit 1
fi

print_msg $GREEN "开始安装依赖..."

# 更新包列表
print_msg $YELLOW "更新包列表..."
apt-get update

# 安装系统依赖
print_msg $YELLOW "安装系统依赖..."
system_deps=(
    "python3-pip"
    "portaudio19-dev"
    "python3-pyaudio"
    "libopenblas-dev"
    "libopenmpi-dev"
    "libasound-dev"
    "ffmpeg"
    "ros-noetic-tf2"
    "ros-noetic-tf2-ros"
    "ros-noetic-tf2-geometry-msgs"
    "python3-tf2-geometry-msgs"
    "flac"
    "mpg123"  # 用于播放 Edge-TTS 生成的 MP3 文件
    "alsa-utils"  # 提供 aplay 命令以检查音频输出设备
    "python3-yaml"    # 添加 yaml 支持
    "python3-tk"     # 添加 tkinter 支持
    "ros-noetic-dynamic-reconfigure"  # 添加动态重配置支持
)

for dep in "${system_deps[@]}"; do
    if ! dpkg -l | grep -q "^ii  $dep "; then
        print_msg $YELLOW "安装 $dep..."
        apt-get install -y $dep
    else
        print_msg $GREEN "$dep 已安装"
    fi
done

# 升级pip
print_msg $YELLOW "升级pip..."
python3 -m pip install --upgrade pip

# 安装Python包
print_msg $YELLOW "安装Python包..."
python_deps=(
    "pyttsx3"
    "edge-tts"  # 用于 Ubuntu 系统的高质量语音合成
    "coqui-tts"
    "pyaudio"
    "vosk"
    "SpeechRecognition"
    "scipy"
    "numpy"
    "langdetect"
    "pyyaml>=5.1"    # 添加 yaml 支持
    "rospkg"         # 添加 ROS 包支持
    "catkin_pkg"     # 添加 catkin 包支持
)

for dep in "${python_deps[@]}"; do
    if ! check_python_package $dep; then
        print_msg $YELLOW "安装 $dep..."
        python3 -m pip install --no-cache-dir $dep
        if [ $? -ne 0 ]; then
            print_msg $RED "警告: $dep 安装失败"
        fi
    else
        print_msg $GREEN "$dep 已安装"
    fi
done

# 安装OpenAI Whisper
print_msg $YELLOW "安装 OpenAI Whisper..."
if ! check_python_package "openai-whisper"; then
    python3 -m pip install --no-cache-dir openai-whisper
fi

# 安装PyTorch
if [[ $(uname -m) == "aarch64" ]]; then
    print_msg $YELLOW "检测到Jetson平台，安装PyTorch..."

    # 设置PyTorch安装URL
    TORCH_URL="https://developer.download.nvidia.cn/compute/redist/jp/v511/pytorch/torch-2.0.0+nv23.05-cp38-cp38-linux_aarch64.whl"

    print_msg $YELLOW "设置LD_LIBRARY_PATH..."
    export LD_LIBRARY_PATH=/usr/lib/llvm-8/lib:$LD_LIBRARY_PATH

    print_msg $YELLOW "安装PyTorch..."
    python3 -m pip install --no-cache --upgrade ${TORCH_URL}

    if [ $? -eq 0 ]; then
        print_msg $GREEN "PyTorch安装成功"
    else
        print_msg $RED "PyTorch安装失败"
    fi
else
    print_msg $YELLOW "非Jetson平台，安装标准版PyTorch..."
    python3 -m pip install torch
fi

# 验证PyTorch安装
print_msg $YELLOW "验证PyTorch安装..."
if python3 -c "import torch; print('PyTorch version:', torch.__version__)"; then
    print_msg $GREEN "PyTorch验证成功"
else
    print_msg $RED "PyTorch验证失败"
fi

# 检查音频设备
print_msg $YELLOW "检查音频设备..."
if ! arecord -l &> /dev/null; then
    print_msg $YELLOW "警告: 未检测到录音设备"
else
    print_msg $GREEN "检测到录音设备"
fi

if ! aplay -l &> /dev/null; then
    print_msg $YELLOW "警告: 未检测到播放设备"
else
    print_msg $GREEN "检测到播放设备"
fi

# 添加权限设置
# print_msg $YELLOW "设置配置文件权限..."
# if [ -f "config/TTSConfig.cfg" ]; then
#     chmod +x config/TTSConfig.cfg
#     print_msg $GREEN "TTSConfig.cfg 权限设置完成"
# fi

# 最后的验证
print_msg $YELLOW "验证所有安装..."
all_deps_installed=true

for dep in "${python_deps[@]}"; do
    if ! check_python_package $dep; then
        print_msg $RED "警告: $dep 安装失败"
        all_deps_installed=false
    fi
done

if [ "$all_deps_installed" = true ]; then
    print_msg $GREEN "所有依赖安装成功！"
else
    print_msg $RED "部分依赖安装失败，请检查上述错误信息"
fi

print_msg $GREEN "安装脚本执行完成！"
print_msg $YELLOW "请注意："
print_msg $YELLOW "1. 如果看到pip权限警告，可以忽略"
print_msg $YELLOW "2. 如果音频设备未就绪，可以稍后插入"
print_msg $YELLOW "3. 可能需要运行: export LD_LIBRARY_PATH=/usr/lib/llvm-8/lib:\$LD_LIBRARY_PATH"
print_msg $YELLOW "4. 建议重新启动终端以确保所有更改生效"
print_msg $YELLOW "5. 如果使用动态重配置功能，请确保已经运行 catkin_make"
# print_msg $YELLOW "6. 确保 config/TTSConfig.cfg 具有可执行权限"
```

### Package: direction_indicator

#### Dependencies (package.xml)

#### CMake Dependencies

- find_package:
  - catkin

#### Launch Files
- launch\direction_indicator.launch

### Package: hoshi_planner

#### Dependencies (package.xml)

- build_depends:
  - nav_core
  - pluginlib
  - roscpp
  - rospy

- exec_depends:
  - nav_core
  - pluginlib
  - roscpp
  - rospy

#### CMake Dependencies

- find_package:
  - Boost
  - catkin

### Package: jie_ware

#### Dependencies (package.xml)

- build_depends:
  - cv_bridge
  - geometry_msgs
  - move_base_msgs
  - nav_msgs
  - roscpp
  - rospy
  - sensor_msgs
  - std_msgs
  - tf

- exec_depends:
  - cv_bridge
  - geometry_msgs
  - move_base_msgs
  - nav_msgs
  - roscpp
  - rospy
  - sensor_msgs
  - std_msgs
  - tf

#### CMake Dependencies

- find_package:
  - Boost
  - OpenCV
  - catkin

#### Launch Files
- launch\amcl_test.launch
- launch\lidar_loc_test.launch

### Package: om_modbus_master

#### Dependencies (package.xml)

- build_depends:
  - message_generation
  - nav_msgs
  - roscpp
  - rospy
  - sensor_msgs
  - std_msgs
  - tf
  - tf2
  - tf2_ros

- exec_depends:
  - message_runtime
  - nav_msgs
  - roscpp
  - rospy
  - sensor_msgs
  - std_msgs
  - tf
  - tf2
  - tf2_ros

#### CMake Dependencies

- find_package:
  - Boost
  - catkin

#### Launch Files
- launch\mobi_con.launch
- launch\om_modbusRTU.launch

### Package: prohibition_areas_plugin

#### Dependencies (package.xml)

- build_depends:
  - boost
  - costmap_2d
  - dynamic_reconfigure
  - geometry_msgs
  - message_generation
  - message_runtime
  - pluginlib
  - roscpp
  - rospack
  - rviz
  - std_srvs
  - tf2_ros
  - xmlrpcpp
  - yaml-cpp

- run_depends:
  - boost
  - costmap_2d
  - dynamic_reconfigure
  - geometry_msgs
  - message_generation
  - message_runtime
  - pluginlib
  - roscpp
  - rospack
  - rviz
  - std_srvs
  - tf2_ros
  - xmlrpcpp
  - yaml-cpp

#### CMake Dependencies

- find_package:
  - Boost
  - Qt5
  - catkin
  - yaml-cpp

#### Launch Files
- launch\edit_prohibition_areas.launch
- launch\prohibition_areas_plugin.launch
- launch\test_prohibition_areas.launch

### Package: rplidar_ros

#### Dependencies (package.xml)

- build_depends:
  - rosconsole
  - roscpp
  - sensor_msgs
  - std_srvs

- run_depends:
  - rosconsole
  - roscpp
  - sensor_msgs
  - std_srvs

#### CMake Dependencies

- find_package:
  - catkin

#### Launch Files
- launch\rplidar_a1.launch
- launch\rplidar_a2m12.launch
- launch\rplidar_a2m7.launch
- launch\rplidar_a2m8.launch
- launch\rplidar_a3.launch
- launch\rplidar_c1.launch
- launch\rplidar_s1.launch
- launch\rplidar_s1_tcp.launch
- launch\rplidar_s2.launch
- launch\rplidar_s2e.launch
- launch\rplidar_s3.launch
- launch\rplidar_t1.launch
- launch\test_rplidar.launch
- launch\test_rplidar_a3.launch
- launch\view_rplidar_a1.launch
- launch\view_rplidar_a2m12.launch
- launch\view_rplidar_a2m7.launch
- launch\view_rplidar_a2m8.launch
- launch\view_rplidar_a3.launch
- launch\view_rplidar_c1.launch
- launch\view_rplidar_s1.launch
- launch\view_rplidar_s1_tcp.launch
- launch\view_rplidar_s2.launch
- launch\view_rplidar_s2e.launch
- launch\view_rplidar_s3.launch
- launch\view_rplidar_t1.launch

### Package: wp_nav_controller

#### Dependencies (package.xml)

- build_depends:
  - actionlib_msgs
  - geometry_msgs
  - message_generation
  - move_base_msgs
  - rospy
  - std_msgs
  - std_srvs
  - tf2_geometry_msgs
  - tf2_ros

- exec_depends:
  - actionlib_msgs
  - amr_waypoint_tools
  - geometry_msgs
  - message_runtime
  - move_base_msgs
  - rospy
  - std_msgs
  - std_srvs
  - tf2_geometry_msgs
  - tf2_ros

#### CMake Dependencies

- find_package:
  - catkin

#### Launch Files
- launch\navi_controller.launch
- launch\waypoint_navigation_go.launch
- launch\wpb_map_tool.launch
- launch\wp_nav_controller.launch
