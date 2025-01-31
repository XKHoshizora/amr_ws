# 使用 ROS Noetic 作为基础镜像
FROM ros:noetic-ros-base-focal as base

# 设置环境变量
ENV DEBIAN_FRONTEND=noninteractive
ENV ROS_DISTRO=noetic
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8

# 设置工作目录
WORKDIR /amr_ws

# 第一阶段：安装系统依赖
FROM base as system-deps

# 安装系统依赖
RUN apt-get update && apt-get install -y --no-install-recommends \
    # 基础开发工具
    build-essential \
    cmake \
    git \
    python3-pip \
    python3-dev \
    wget \
    unzip \
    # USB和蓝牙相关
    udev \
    bluez \
    bluetooth \
    libbluetooth-dev \
    # 网络工具
    net-tools \
    iproute2 \
    iputils-ping \
    # 摄像头支持
    v4l-utils \
    # ROS 基础包
    ros-${ROS_DISTRO}-map-server \
    ros-${ROS_DISTRO}-navigation \
    ros-${ROS_DISTRO}-tf2 \
    ros-${ROS_DISTRO}-tf2-ros \
    ros-${ROS_DISTRO}-tf2-geometry-msgs \
    python3-tf2-geometry-msgs \
    ros-${ROS_DISTRO}-dynamic-reconfigure \
    # 音频相关依赖
    portaudio19-dev \
    python3-pyaudio \
    libasound-dev \
    ffmpeg \
    flac \
    mpg123 \
    alsa-utils \
    # Qt相关依赖
    qtbase5-dev \
    qt5-qmake \
    libqt5core5a \
    # 其他系统依赖
    libopenblas-dev \
    libopenmpi-dev \
    python3-yaml \
    python3-tk \
    libboost-all-dev \
    libeigen3-dev \
    libopencv-dev \
    libyaml-cpp-dev \
    && rm -rf /var/lib/apt/lists/*

# 第二阶段：安装Python依赖
FROM system-deps as python-deps

# 升级pip并安装Python包
RUN python3 -m pip install --no-cache-dir --upgrade pip && \
    python3 -m pip install --no-cache-dir \
    pyttsx3 \
    edge-tts \
    coqui-tts \
    pyaudio \
    vosk \
    SpeechRecognition \
    scipy \
    numpy \
    langdetect \
    pyyaml>=5.1 \
    rospkg \
    catkin_pkg \
    openai-whisper \
    torch \
    PySide6 \
    matplotlib \
    pandas \
    psutil \
    pyqtgraph \
    pytest \
    opencv-python

# 第三阶段：构建工作空间
FROM python-deps as workspace

# 复制工作空间文件
COPY src/amr_controller ./src/amr_controller
COPY src/amr_description ./src/amr_description
COPY src/amr_imu_filters ./src/amr_imu_filters
COPY src/amr_laser_filters ./src/amr_laser_filters
COPY src/amr_launcher ./src/amr_launcher
COPY src/amr_lidar_localization ./src/amr_lidar_localization
COPY src/amr_map ./src/amr_map
COPY src/amr_monitor ./src/amr_monitor
COPY src/amr_navi ./src/amr_navi
COPY src/amr_nova ./src/amr_nova
COPY src/amr_slam ./src/amr_slam
COPY src/amr_waypoint_tools ./src/amr_waypoint_tools
COPY src/audio_compass ./src/audio_compass
COPY src/direction_indicator ./src/direction_indicator
COPY src/hoshi_planner ./src/hoshi_planner
COPY src/jie_ware ./src/jie_ware
COPY src/om_modbus_master ./src/om_modbus_master
COPY src/prohibition_areas_plugin ./src/prohibition_areas_plugin
COPY src/rplidar_ros ./src/rplidar_ros
COPY src/wp_nav_controller ./src/wp_nav_controller

# 创建必要的目录
RUN mkdir -p src/amr_monitor/config && \
    mkdir -p src/amr_monitor/data && \
    mkdir -p src/audio_compass/models

# 下载并解压 Vosk 模型
RUN cd src/audio_compass/models && \
    # 下载英语模型
    wget https://alphacephei.com/vosk/models/vosk-model-en-us-0.22.zip && \
    unzip vosk-model-en-us-0.22.zip && \
    rm vosk-model-en-us-0.22.zip && \
    # 下载中文模型
    wget https://alphacephei.com/vosk/models/vosk-model-cn-0.22.zip && \
    unzip vosk-model-cn-0.22.zip && \
    rm vosk-model-cn-0.22.zip && \
    # 下载日语模型
    wget https://alphacephei.com/vosk/models/vosk-model-ja-0.22.zip && \
    unzip vosk-model-ja-0.22.zip && \
    rm vosk-model-ja-0.22.zip

# 设置权限
RUN find . -type f -name "*.sh" -exec chmod +x {} \; && \
    find . -type f -name "*.py" -exec chmod +x {} \;

# 初始化工作空间并构建
RUN /bin/bash -c '. /opt/ros/${ROS_DISTRO}/setup.bash && \
    catkin_make'

# 最终阶段：运行环境
FROM workspace as runtime

# 复制 udev 规则
COPY om_controller.rules /etc/udev/rules.d/
COPY rplidar.rules /etc/udev/rules.d/

# 设置设备权限
RUN chmod 666 /etc/udev/rules.d/om_controller.rules && \
    chmod 666 /etc/udev/rules.d/rplidar.rules

# 设置启动脚本
COPY ./docker_entrypoint.sh /
RUN chmod +x /docker_entrypoint.sh

# 设置环境变量
ENV LD_LIBRARY_PATH=/usr/lib/llvm-8/lib:$LD_LIBRARY_PATH

# 设置入口点
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["bash"]
