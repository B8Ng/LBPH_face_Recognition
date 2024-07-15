import os
import cv2
from PIL import Image
import numpy as np


def getImageAndLabels(path):
    facesSamples = []
    ids = []

    # 加载Haar级联分类器用于人脸检测
    face_detector = cv2.CascadeClassifier('F:\Anaconda\envs\pytorch\Lib\site-packages\cv2\data\haarcascade_frontalface_alt.xml')

    # 遍历主目录下的所有子文件夹
    for subdir in os.listdir(path):
        subdir_path = os.path.join(path, subdir)
        if os.path.isdir(subdir_path):
            # 从子文件夹名称提取标签ID
            id = int(subdir.split('s')[1])
            # 遍历子文件夹中的每张图片
            for f in os.listdir(subdir_path):
                try:
                    imagePath = os.path.join(subdir_path, f)
                    # 打开图片并转换为灰度图
                    PIL_img = Image.open(imagePath).convert('L')
                    # 将灰度图转换为numpy数组
                    img_numpy = np.array(PIL_img, 'uint8')
                    # 检测人脸
                    faces = face_detector.detectMultiScale(img_numpy)
                    for x, y, w, h in faces:
                        # 将检测到的人脸区域添加到facesSamples列表
                        facesSamples.append(img_numpy[y:y + h, x:x + w])
                        # 将对应的标签ID添加到ids列表
                        ids.append(id)
                except Exception as e:
                    print(f"处理文件 {imagePath} 时出错: {e}")
    return facesSamples, ids


def train(path):
    faces, ids = getImageAndLabels(path)
    # 创建LBPH人脸识别器对象
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    # 训练识别器，参数为图像数组和标签数组
    recognizer.train(faces, np.array(ids))
    write_path = "trainer/trainer.yml"
    # 保存训练好的模型
    recognizer.write(write_path)
    print(f"训练完成!模型保存地址为:{write_path}")

if __name__ == '__main__':
    # 图片路径
    path = './data/train'
    train(path)




