import os
import shutil


def ship_exist(file_path):
    """
    检测给定路径的文件是否包含特定字符串 "ship"。
    
    参数:
    file_path (str): 文件的路径
    
    返回:
    bool: 如果文件包含 "ship"，返回 True；否则返回 False
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                if line.startswith('1 '):
                    return True
        return False
    except FileNotFoundError:
        print(f"文件 {file_path} 未找到。")
        return False
    except Exception as e:
        print(f"读取文件 {file_path} 时发生错误: {e}")
        return False


def copy_train(label_file_path):
    """
    将 label 文件夹中的 txt 文件和对应的 pic 文件夹中的 jpg 文件复制到目标文件夹。
    
    参数:
    label_file_path (str): label 文件夹中 txt 文件的路径
    """
    try:
        base_path = os.path.dirname(label_file_path)
        # 提取文件名
        file_name = os.path.basename(label_file_path)
        base_name = os.path.splitext(file_name)[0]
        
        # 构建对应的图片文件路径
        pic_file_path = os.path.join(base_path,'..','..','images','train', base_name + '.jpg')
        
        # 构建目标文件夹路径
        label_copy_dir = os.path.join(base_path,'..','..','labels_copy','train')
        pic_copy_dir = os.path.join(base_path,'..','..','images_copy','train')
        
        # 创建目标文件夹（如果不存在）
        # os.makedirs(label_copy_dir, exist_ok=True)
        # os.makedirs(pic_copy_dir, exist_ok=True)
        
        # 复制 label 文件
        shutil.copy(label_file_path, label_copy_dir)
        
        # 复制 pic 文件
        if os.path.exists(pic_file_path):
            shutil.copy(pic_file_path, pic_copy_dir)
        else:
            print(f"对应的图片文件 {pic_file_path} 未找到。")
    except Exception as e:
        print(f"复制文件时发生错误: {e}")


def copy_val(label_file_path):
    """
    将 label 文件夹中的 txt 文件和对应的 pic 文件夹中的 jpg 文件复制到目标文件夹。
    
    参数:
    label_file_path (str): label 文件夹中 txt 文件的路径
    """
    try:
        base_path = os.path.dirname(label_file_path)
        # 提取文件名
        file_name = os.path.basename(label_file_path)
        base_name = os.path.splitext(file_name)[0]
        
        # 构建对应的图片文件路径
        pic_file_path = os.path.join(base_path,'..','..','images','val', base_name + '.jpg')
        
        # 构建目标文件夹路径
        label_copy_dir = os.path.join(base_path,'..','..','labels_copy','val')
        pic_copy_dir = os.path.join(base_path,'..','..','images_copy','val')
        
        # 创建目标文件夹（如果不存在）
        # os.makedirs(label_copy_dir, exist_ok=True)
        # os.makedirs(pic_copy_dir, exist_ok=True)
        
        # 复制 label 文件
        shutil.copy(label_file_path, label_copy_dir)
        
        # 复制 pic 文件
        if os.path.exists(pic_file_path):
            shutil.copy(pic_file_path, pic_copy_dir)
        else:
            print(f"对应的图片文件 {pic_file_path} 未找到。")
    except Exception as e:
        print(f"复制文件时发生错误: {e}")


def main():
    # file_path = 'C:/baidunetdiskdownload/DOTA-Merge-Split/labels/train/P1200__1024__2620___2620.txt'
    # 计数器
    train_file_count = 0
    train_file_exclude = 0
    val_file_count = 0
    val_file_exclude = 0

    # 处理 train 文件夹
    for file in os.listdir('C:/baidunetdiskdownload/DOTA-Merge-Split/labels/train/'):
        file_path = os.path.join('C:/baidunetdiskdownload/DOTA-Merge-Split/labels/train/', file)
        if ship_exist(file_path):
            copy_train(file_path)
            train_file_count += 1
            print(f"文件 {file_path} 包含 'ship'。")
        else:
            # print(f"文件 {file_path} 不包含 'ship'。")
            train_file_exclude += 1
    # train统计信息
    # 会被覆盖
    # print(f"train 文件夹中包含 'ship' 的文件数: {train_file_count}")
    # print(f"train 文件夹中不包含 'ship' 的文件数: {train_file_exclude}")

    # 处理 val 文件夹
    for file in os.listdir('C:/baidunetdiskdownload/DOTA-Merge-Split/labels/val/'):
        file_path = os.path.join('C:/baidunetdiskdownload/DOTA-Merge-Split/labels/val/', file)
        if ship_exist(file_path):
            copy_val(file_path)
            val_file_count += 1
            print(f"文件 {file_path} 包含 'ship'。")
        else:
            # print(f"文件 {file_path} 不包含 'ship'。")
            val_file_exclude += 1
    # 全部统计信息
    print(f"train 文件夹中包含 'ship' 的文件数: {train_file_count}")
    print(f"train 文件夹中不包含 'ship' 的文件数: {train_file_exclude}")
    print(f"val 文件夹中包含 'ship' 的文件数: {val_file_count}")
    print(f"val 文件夹中不包含 'ship' 的文件数: {val_file_exclude}")


if __name__ == '__main__':
    main()
                    