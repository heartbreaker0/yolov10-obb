import os

def filter_txt_files(folder_path):
    count = 0
    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        # 检查文件是否为txt文件
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            # 读取文件内容
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
            # 过滤掉不以1_开头的行
            filtered_lines = [line for line in lines if line.startswith('1 ')]
            # 将过滤后的内容写回文件
            with open(file_path, 'w', encoding='utf-8') as file:
                file.writelines(filtered_lines)
        count += 1
    return count


def replace_ID(folder_path):
    count = 0
    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        # 检查文件是否为txt文件
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            # 读取文件内容
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
            # 将每行开头的1_替换为0_
            modified_lines = [line.replace('1 ', '0 ', 1) if line.startswith('1 ') else line for line in lines]
            # 将修改后的内容写回文件
            with open(file_path, 'w', encoding='utf-8') as file:
                file.writelines(modified_lines)
        count += 1
    return count



def main():
    print(filter_txt_files('C:/baidunetdiskdownload/DOTA-Merge-Split-Extract/labels/train'))
    print(filter_txt_files('C:/baidunetdiskdownload/DOTA-Merge-Split-Extract/labels/val'))
    print(replace_ID('C:/baidunetdiskdownload/DOTA-Merge-Split-Extract/labels/train'))
    print(replace_ID('C:/baidunetdiskdownload/DOTA-Merge-Split-Extract/labels/val'))
        
        
if __name__ == '__main__':
    main()
