import os
import argparse
import glob
import sys
import codecs
from bagpy import bagreader
import pandas as pd
import shutil

# 设置控制台输出编码
if sys.stdout.encoding != 'utf-8':
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

def get_project_root():
    """
    获取项目根目录的绝对路径
    """
    current_path = os.path.abspath(__file__)
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(current_path)))
    return project_root

def extract_bag_data(bag_path, output_path, format='excel'):
    """
    从bag文件中提取数据并保存为指定格式
    """
    if not os.path.exists(bag_path):
        print(f"错误: 输入文件 {bag_path} 不存在")
        return False

    try:
        print(f"正在处理文件: {bag_path}")
        
        # 创建 bag 读取器
        bag = bagreader(bag_path)
        
        # 获取话题列表
        print("可用的话题:")
        for topic in bag.topics:
            print(f"  - {topic}")
            
        if format == 'excel':
            # 准备Excel数据
            excel_data = {}
            
            # 提取数据
            try:
                cmd_vel_data = pd.read_csv(bag.message_by_topic('/cmd_vel'))
                print(f"成功读取 cmd_vel 数据, 数据点数: {len(cmd_vel_data)}")
                excel_data['cmd_vel'] = cmd_vel_data
            except Exception as e:
                print(f"读取 cmd_vel 数据时出错: {str(e)}")
            
            try:
                odom_data = pd.read_csv(bag.message_by_topic('/odom'))
                print(f"成功读取 odom 数据, 数据点数: {len(odom_data)}")
                excel_data['odom'] = odom_data
            except Exception as e:
                print(f"读取 odom 数据时出错: {str(e)}")

            # 保存为Excel文件
            if excel_data:
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                excel_file = output_path + '.xlsx'
                with pd.ExcelWriter(excel_file) as writer:
                    for sheet_name, data in excel_data.items():
                        data.to_excel(writer, sheet_name=sheet_name, index=False)
                print(f"数据已保存到: {excel_file}")
            
        else:
            # 为CSV创建一个同名文件夹
            folder_name = os.path.splitext(os.path.basename(bag_path))[0]
            output_folder = os.path.join(os.path.dirname(output_path), folder_name)
            
            # 如果文件夹已存在，先删除它
            if os.path.exists(output_folder):
                shutil.rmtree(output_folder)
            
            # 创建新文件夹
            os.makedirs(output_folder)
            print(f"创建输出文件夹: {output_folder}")
            
            # 提取并保存数据
            success = False
            
            try:
                cmd_vel_data = pd.read_csv(bag.message_by_topic('/cmd_vel'))
                cmd_vel_file = os.path.join(output_folder, 'cmd_vel.csv')
                cmd_vel_data.to_csv(cmd_vel_file, index=False, encoding='utf-8')
                print(f"已保存 cmd_vel 数据, 数据点数: {len(cmd_vel_data)}")
                success = True
            except Exception as e:
                print(f"读取或保存 cmd_vel 数据时出错: {str(e)}")
            
            try:
                odom_data = pd.read_csv(bag.message_by_topic('/odom'))
                odom_file = os.path.join(output_folder, 'odom.csv')
                odom_data.to_csv(odom_file, index=False, encoding='utf-8')
                print(f"已保存 odom 数据, 数据点数: {len(odom_data)}")
                success = True
            except Exception as e:
                print(f"读取或保存 odom 数据时出错: {str(e)}")
            
            if not success:
                print("错误: 未能成功保存任何数据")
                if os.path.exists(output_folder):
                    shutil.rmtree(output_folder)
                return False
            
            print(f"所有数据已保存到文件夹: {output_folder}")

        return True

    except Exception as e:
        print(f"处理文件时发生错误: {str(e)}")
        return False

def process_directory(directory):
    """
    处理指定目录下的所有bag文件
    """
    directory = os.path.abspath(directory)
    
    if not os.path.exists(directory):
        print(f"错误: 目录不存在: {directory}")
        print(f"当前工作目录: {os.getcwd()}")
        return False

    bag_files = glob.glob(os.path.join(directory, "*.bag"))
    
    if not bag_files:
        print(f"警告: 在目录中没有找到.bag文件: {directory}")
        return False

    print(f"找到 {len(bag_files)} 个.bag文件:")
    for bag_file in bag_files:
        print(f"  - {os.path.basename(bag_file)}")
    
    success_count = 0
    for bag_file in bag_files:
        base_name = os.path.splitext(bag_file)[0]
        if extract_bag_data(bag_file, base_name, format='csv'):
            success_count += 1

    print(f"\n处理完成: 成功处理 {success_count}/{len(bag_files)} 个文件")
    return True

if __name__ == "__main__":
    # 设置命令行输出编码
    os.environ['PYTHONIOENCODING'] = 'utf-8'
    
    # 获取项目根目录
    project_root = get_project_root()
    data_default_path = os.path.join(project_root, "data")
    navi_data_path = os.path.join(data_default_path, "navigation_data")
    slam_data_path = os.path.join(data_default_path, "slam_data")

    print("工作环境信息:")
    print(f"当前工作目录: {os.getcwd()}")
    print(f"项目根目录: {project_root}")
    print(f"默认数据目录: {data_default_path}")
    print(f"导航数据目录: {navi_data_path}")
    print()

    parser = argparse.ArgumentParser(description="从指定的 .bag 文件或目录中提取 /cmd_vel 和 /odom 话题数据")
    parser.add_argument(
        "--file",
        help="单个.bag文件的路径"
    )
    parser.add_argument(
        "--dir",
        default=navi_data_path,
        help=f"包含.bag文件的目录路径 (默认: {navi_data_path})"
    )
    parser.add_argument(
        "--output",
        help="输出文件的路径（仅在处理单个文件时使用）"
    )
    parser.add_argument(
        "--format",
        choices=['excel', 'csv'],
        default='csv',
        help="输出文件格式 (默认: csv)"
    )
    
    args = parser.parse_args()

    if args.file:
        file_path = os.path.abspath(args.file)
        output_file = args.output or os.path.splitext(file_path)[0]
        if not extract_bag_data(file_path, output_file, args.format):
            sys.exit(1)
    else:
        if not process_directory(args.dir):
            sys.exit(1)

    sys.exit(0)