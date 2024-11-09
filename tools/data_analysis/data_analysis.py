import pandas as pd
import matplotlib.pyplot as plt
import os
from pathlib import Path
from typing import Optional, List
import logging
import sys

# 配置日志记录，设置编码为UTF-8
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(stream=sys.stdout)
    ]
)
# 设置标准输出编码为UTF-8
sys.stdout.reconfigure(encoding='utf-8')
logger = logging.getLogger(__name__)

class DataAnalysisBase:
    """数据分析基础类，提供基本的数据加载和图表保存功能"""
    
    def __init__(self, data_path: Path):
        self.data_path = Path(data_path)
        self.data: Optional[pd.DataFrame] = None
        self.output_dir = self.data_path.parent / 'plots'
        self.output_dir.mkdir(parents=True, exist_ok=True)
    
    def load_data(self):
        """加载并预处理CSV数据文件"""
        try:
            if not self.data_path.exists():
                raise FileNotFoundError(f"数据文件不存在：{self.data_path}")
                
            self.data = pd.read_csv(self.data_path)
            self.data['Time'] = self.data['Time'] - self.data['Time'].iloc[0]
            logger.info(f"成功加载数据：{self.data_path}")
        except Exception as e:
            logger.error(f"加载数据失败 {self.data_path}: {str(e)}")
            raise

    def save_plot(self, plt, filename: str):
        """保存图表到输出目录"""
        try:
            plot_path = self.output_dir / filename
            plt.savefig(plot_path)
            plt.close()
            logger.info(f"成功保存图表：{plot_path}")
        except Exception as e:
            logger.error(f"保存图表失败 {filename}: {str(e)}")
            plt.close()
            raise

class CmdVelAnalysis(DataAnalysisBase):
    """速度指令(cmd_vel)数据分析类"""

    def plot_linear_velocity(self):
        """绘制线速度图表"""
        plt.figure(figsize=(10, 5))
        plt.plot(self.data['Time'], self.data['linear.x'], 
                label='Linear Velocity (x)', linestyle='-', marker='o', color='blue')
        plt.xlabel('Time (s)')
        plt.ylabel('Linear Velocity (x)')
        plt.title('Linear Velocity (x) over Time')
        plt.legend()
        plt.grid(True)
        self.save_plot(plt, 'cmd_vel_linear_velocity.png')
    
    def plot_angular_velocity(self):
        """绘制角速度图表"""
        plt.figure(figsize=(10, 5))
        plt.plot(self.data['Time'], self.data['angular.z'], 
                label='Angular Velocity (z)', linestyle='-', marker='x', color='orange')
        plt.xlabel('Time (s)')
        plt.ylabel('Angular Velocity (z)')
        plt.title('Angular Velocity (z) over Time')
        plt.legend()
        plt.grid(True)
        self.save_plot(plt, 'cmd_vel_angular_velocity.png')
    
    def plot_combined_velocity(self):
        """绘制组合速度图表（线速度和角速度）"""
        plt.figure(figsize=(10, 5))
        plt.plot(self.data['Time'], self.data['linear.x'], 
                label='Linear Velocity (x)', linestyle='-', marker='o', color='blue')
        plt.plot(self.data['Time'], self.data['angular.z'], 
                label='Angular Velocity (z)', linestyle='-', marker='x', color='red')
        plt.xlabel('Time (s)')
        plt.ylabel('Velocity')
        plt.title('Linear and Angular Velocity over Time')
        plt.legend()
        plt.grid(True)
        self.save_plot(plt, 'cmd_vel_combined_velocity.png')

class OdomAnalysis(DataAnalysisBase):
    """里程计(odometry)数据分析类"""
    
    def load_data(self):
        """重写数据加载方法，处理里程计特定的数据预处理"""
        super().load_data()
        numeric_columns = [
            'pose.pose.position.x',
            'pose.pose.position.y',
            'twist.twist.linear.x',
            'twist.twist.angular.z'
        ]
        for col in numeric_columns:
            self.data[col] = pd.to_numeric(self.data[col], errors='coerce')

    def plot_trajectory(self):
        """绘制机器人运动轨迹图"""
        plt.figure(figsize=(10, 5))
        plt.plot(self.data['pose.pose.position.x'], self.data['pose.pose.position.y'], 
                label='Trajectory', color='blue')
        plt.xlabel('Position X (m)')
        plt.ylabel('Position Y (m)')
        plt.title('Robot Trajectory (Position X vs Position Y)')
        plt.legend()
        plt.grid(True)
        self.save_plot(plt, 'odom_trajectory.png')

    def plot_linear_velocity(self):
        """绘制线速度图表"""
        plt.figure(figsize=(10, 5))
        plt.plot(self.data['Time'], self.data['twist.twist.linear.x'], 
                label='Linear Velocity (x)', linestyle='-', marker='o', color='green')
        plt.xlabel('Time (s)')
        plt.ylabel('Linear Velocity (x)')
        plt.title('Linear Velocity (x) over Time')
        plt.legend()
        plt.grid(True)
        self.save_plot(plt, 'odom_linear_velocity.png')

    def plot_angular_velocity(self):
        """绘制角速度图表"""
        plt.figure(figsize=(10, 5))
        plt.plot(self.data['Time'], self.data['twist.twist.angular.z'], 
                label='Angular Velocity (z)', linestyle='-', marker='x', color='red')
        plt.xlabel('Time (s)')
        plt.ylabel('Angular Velocity (z)')
        plt.title('Angular Velocity (z) over Time')
        plt.legend()
        plt.grid(True)
        self.save_plot(plt, 'odom_angular_velocity.png')

    def plot_combined_velocity(self):
        """绘制组合速度图表（线速度和角速度）"""
        plt.figure(figsize=(10, 5))
        plt.plot(self.data['Time'], self.data['twist.twist.linear.x'], 
                label='Linear Velocity (x)', linestyle='-', marker='o', color='green')
        plt.plot(self.data['Time'], self.data['twist.twist.angular.z'], 
                label='Angular Velocity (z)', linestyle='-', marker='x', color='red')
        plt.xlabel('Time (s)')
        plt.ylabel('Velocity')
        plt.title('Linear and Angular Velocity over Time')
        plt.legend()
        plt.grid(True)
        self.save_plot(plt, 'odom_combined_velocity.png')

def find_data_directories(base_dir: Path) -> List[Path]:
    """查找包含所需CSV文件的数据目录"""
    try:
        base_dir = Path(base_dir)
        if not base_dir.exists():
            logger.error(f"基础目录不存在：{base_dir}")
            return []
            
        data_dirs = []
        
        for path in base_dir.rglob('*'):
            if path.is_dir():
                cmd_vel_file = path / 'cmd_vel.csv'
                odom_file = path / 'odom.csv'
                if cmd_vel_file.exists() and odom_file.exists():
                    data_dirs.append(path)
                    logger.info(f"找到有效数据目录：{path}")
        
        if not data_dirs:
            logger.warning(f"在 {base_dir} 中未找到有效的数据目录")
        else:
            logger.info(f"共找到 {len(data_dirs)} 个有效的数据目录")
            
        return data_dirs
    except Exception as e:
        logger.error(f"搜索数据目录时出错: {str(e)}")
        return []

def main():
    """主函数：处理所有数据目录中的数据并生成图表"""
    try:
        current_file = Path(__file__).resolve()
        logger.info(f"当前脚本路径：{current_file}")
        
        project_root = current_file.parents[2]
        logger.info(f"项目根目录：{project_root}")
        
        nav_data_dir = project_root / 'data' / 'navigation_data'
        logger.info(f"导航数据目录：{nav_data_dir}")
        
        if not nav_data_dir.exists():
            raise FileNotFoundError(f"导航数据目录不存在：{nav_data_dir}")
        
        data_dirs = find_data_directories(nav_data_dir)
        
        if not data_dirs:
            logger.error("未找到任何有效的数据目录")
            return
            
        for data_dir in data_dirs:
            logger.info(f"\n开始处理目录: {data_dir}")
            
            try:
                cmd_vel_path = data_dir / 'cmd_vel.csv'
                if cmd_vel_path.exists():
                    logger.info(f"处理速度指令数据：{cmd_vel_path}")
                    cmd_vel_analysis = CmdVelAnalysis(cmd_vel_path)
                    cmd_vel_analysis.load_data()
                    cmd_vel_analysis.plot_linear_velocity()
                    cmd_vel_analysis.plot_angular_velocity()
                    cmd_vel_analysis.plot_combined_velocity()
                else:
                    logger.warning(f"速度指令数据文件不存在：{cmd_vel_path}")
                
                odom_path = data_dir / 'odom.csv'
                if odom_path.exists():
                    logger.info(f"处理里程计数据：{odom_path}")
                    odom_analysis = OdomAnalysis(odom_path)
                    odom_analysis.load_data()
                    odom_analysis.plot_trajectory()
                    odom_analysis.plot_linear_velocity()
                    odom_analysis.plot_angular_velocity()
                    odom_analysis.plot_combined_velocity()
                else:
                    logger.warning(f"里程计数据文件不存在：{odom_path}")
                    
            except Exception as e:
                logger.error(f"处理目录 {data_dir} 时出错: {str(e)}")
                continue
            
    except Exception as e:
        logger.error(f"主程序执行时发生致命错误: {str(e)}")
        raise

if __name__ == '__main__':
    main()