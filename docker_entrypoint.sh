#!/bin/bash
set -e

# 设置ROS环境
source "/opt/ros/$ROS_DISTRO/setup.bash"
source "/amr_ws/devel/setup.bash"

exec "$@"
