import os
import random
import shutil

# 设置路径
root_dir = "data/jm"
output_root_dir = "data"  # 输出的根路径
train_dir = os.path.join(output_root_dir, "train")
test_dir = os.path.join(output_root_dir, "test")

# 创建训练集和测试集文件夹
os.makedirs(train_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

# 遍历所有文件夹
for i in range(1, 41):
    folder_name = f"s{i}"
    folder_path = os.path.join(root_dir, folder_name)
    if not os.path.exists(folder_path):
        continue

    # 获取文件夹中的所有文件
    files = [f for f in os.listdir(folder_path) if f.endswith('.pgm')]

    # 打乱文件顺序
    random.shuffle(files)

    # 计算训练集和测试集的分界点
    split_point = int(len(files) * 0.8)

    # 分割文件
    train_files = files[:split_point]
    test_files = files[split_point:]

    # 复制训练集文件到训练集文件夹
    train_folder_path = os.path.join(train_dir, folder_name)
    os.makedirs(train_folder_path, exist_ok=True)
    for file in train_files:
        shutil.copy(os.path.join(folder_path, file), os.path.join(train_folder_path, file))

    # 复制测试集文件到测试集文件夹
    test_folder_path = os.path.join(test_dir, folder_name)
    os.makedirs(test_folder_path, exist_ok=True)
    for file in test_files:
        shutil.copy(os.path.join(folder_path, file), os.path.join(test_folder_path, file))

print("数据集划分完成！")
