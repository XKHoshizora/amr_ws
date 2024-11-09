# ROS Bag Data Extractor & Analyzer

这是一个用于从 ROS bag 文件中提取话题数据并进行分析的 Python 工具集。该工具集可以自动处理单个或多个 bag 文件，提取关键数据，并生成可视化分析图表。

## 功能特点

### 数据提取 (rosbag_data_extraction.py)
- 支持提取 `/cmd_vel` 和 `/odom` 话题数据
- 可以处理单个 bag 文件或批量处理整个目录
- 支持两种输出格式：
  - CSV 格式：为每个 bag 文件创建独立文件夹，分别存储不同话题的数据
  - Excel 格式：将所有话题数据保存在同一个 Excel 文件的不同表格中
- 自动检测和显示 bag 文件中的可用话题
- 提供详细的处理进度和错误信息
- 支持命令行参数配置

### 数据分析 (data_analysis.py)
- 自动处理从 bag 文件中提取的 CSV 数据
- 生成多种可视化图表：
  - 线速度随时间变化图
  - 角速度随时间变化图
  - 线速度和角速度组合图
  - 机器人运动轨迹图（仅用于里程计数据）
- 自动在数据目录下创建 `plots` 文件夹存储图表
- 支持批量处理多个数据集
- 提供详细的处理日志

## 目录结构

```
amr_ws/
├── data/
│   ├── navigation_data/
│   │   ├── navi_data1.bag
│   │   ├── navi_data2.bag
│   │   ├── navi_data1/
│   │   │   ├── plots/
│   │   │   │   ├── cmd_vel_linear_velocity.png
│   │   │   │   ├── cmd_vel_angular_velocity.png
│   │   │   │   ├── cmd_vel_combined_velocity.png
│   │   │   │   ├── odom_trajectory.png
│   │   │   │   ├── odom_linear_velocity.png
│   │   │   │   ├── odom_angular_velocity.png
│   │   │   │   └── odom_combined_velocity.png
│   │   │   ├── cmd_vel.csv
│   │   │   └── odom.csv
│   │   └── navi_data2/
│   │       └── [类似的结构]
│   └── slam_data/
└── tools/
    └── data_analysis/
        ├── rosbag_data_extraction.py
        └── data_analysis.py
```

## 依赖项

- Python 3.x
- bagpy
- pandas
- numpy
- matplotlib
- pathlib

### 安装依赖

```bash
pip install bagpy pandas numpy matplotlib
```

## 使用方法

### 1. 数据提取工具 (rosbag_data_extraction.py)

#### 基本用法

处理默认目录（amr_ws/data/navigation_data/）下的所有 bag 文件：

```bash
python rosbag_data_extraction.py
```

#### 命令行参数

- `--file`：指定单个 bag 文件的路径
- `--dir`：指定包含 bag 文件的目录路径
- `--output`：指定输出文件的路径（仅在处理单个文件时使用）
- `--format`：指定输出格式（'csv' 或 'excel'，默认为 'csv'）

#### 示例

1. 处理单个 bag 文件：
```bash
python rosbag_data_extraction.py --file path/to/your.bag
```

2. 处理指定目录：
```bash
python rosbag_data_extraction.py --dir path/to/directory
```

3. 生成 Excel 格式输出：
```bash
python rosbag_data_extraction.py --format excel
```

### 2. 数据分析工具 (data_analysis.py)

#### 基本用法

直接运行脚本分析所有提取的数据：

```bash
python data_analysis.py
```

程序会自动：
1. 搜索导航数据目录
2. 查找包含 CSV 文件的有效数据目录
3. 为每个数据目录创建 `plots` 子目录
4. 生成并保存所有分析图表

#### 输出图表

每个数据集会生成以下图表：

1. CMD_VEL 数据图表：
   - `cmd_vel_linear_velocity.png`: 线速度时间序列图
   - `cmd_vel_angular_velocity.png`: 角速度时间序列图
   - `cmd_vel_combined_velocity.png`: 组合速度图

2. ODOM 数据图表：
   - `odom_trajectory.png`: 机器人运动轨迹图
   - `odom_linear_velocity.png`: 实际线速度时间序列图
   - `odom_angular_velocity.png`: 实际角速度时间序列图
   - `odom_combined_velocity.png`: 实际组合速度图

## 输出格式

### CSV 格式（默认）
为每个 bag 文件创建一个同名文件夹，包含各个话题的独立 CSV 文件：
```
navi_data1/
├── cmd_vel.csv
└── odom.csv
```

### Excel 格式
生成单个 Excel 文件，不同话题数据存储在不同的表格中：
```
navi_data1.xlsx
├── cmd_vel (sheet)
└── odom (sheet)
```

## 完整工作流程

1. 使用 rosbag_data_extraction.py 从 bag 文件中提取数据：
```bash
python rosbag_data_extraction.py
```

2. 使用 data_analysis.py 分析提取的数据并生成图表：
```bash
python data_analysis.py
```

## 注意事项

### 数据提取
1. CSV 格式输出时会自动创建新的文件夹，如果同名文件夹已存在会被覆盖
2. 所有输出文件默认使用 UTF-8 编码
3. 如果处理过程中出现错误，程序会提供详细的错误信息
4. 确保具有足够的磁盘空间和文件夹写入权限

### 数据分析
1. 确保输入的 CSV 文件格式正确：
   - cmd_vel.csv 需要包含 Time、linear.x、angular.z 列
   - odom.csv 需要包含 Time、pose.pose.position.x/y、twist.twist.linear.x、twist.twist.angular.z 列
2. 图表会自动保存在对应数据目录的 plots 子文件夹中
3. 如果 plots 文件夹已存在，会在其中添加新的图表
4. 所有错误和警告信息会记录在控制台输出中

## 错误处理

- 程序会检查输入文件和目录是否存在
- 如果未找到 bag 文件或 CSV 文件，会显示警告信息
- 处理失败时会显示具体的错误原因
- 数据提取时，如果 CSV 格式输出失败，会自动清理已创建的文件夹
- 数据分析时，单个数据集的处理错误不会影响其他数据集的分析

## 贡献

欢迎提交问题报告和改进建议。如需贡献代码，请确保遵循以下原则：
- 保持代码风格一致
- 添加适当的注释和文档
- 确保新功能有足够的错误处理

## 作者

Hoshizora

## 许可证

[MIT License](https://opensource.org/licenses/MIT)