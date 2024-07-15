import cv2 as cv
import os
import random


def get_image_path_by_id(label_id):
    """
    根据标签ID从训练数据集中获取对应的文件路径
    """
    train_data_path = "./data/train"
    folder_name = f"s{label_id}"
    folder_path = os.path.abspath(os.path.join(train_data_path, folder_name))

    if os.path.isdir(folder_path):
        files = os.listdir(folder_path)
        if files:
            # 随机选择一个文件返回绝对路径
            return os.path.abspath(os.path.join(folder_path, random.choice(files)))
    return None


def forecast(path):
    recognizer = cv.face.LBPHFaceRecognizer_create()
    # 加载数据
    recognizer.read('trainer/trainer.yml')
    # 准备识别的图片
    img = cv.imread(path)
    # 图片灰度转换
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # 加载特征数据
    face_detector = cv.CascadeClassifier("F:\Anaconda\envs\pytorch\Lib\site-packages\cv2\data\haarcascade_frontalface_alt.xml")
    faces = face_detector.detectMultiScale(gray)
    label_path = None
    for x, y, w, h in faces:
        #cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # 人脸识别
        # predict该函数返回两个元素的数组：第一个元素是所识别个体的标签，第二个是置信度评分
        id, confidence = recognizer.predict(gray[y:y + h, x:x + w])
        print('标签id:', id, '置信评分：', confidence)
        if confidence >= 116:
            print(f"{id}置信评分过高,识别可能不准确")
        # 获取标签对应的文件路径
        label_path = get_image_path_by_id(id)
        break  # 只处理第一个检测到的人脸
    # 显示图片
    #cv.imshow('result', img)
    # 设置等待键盘输入
    #cv.waitKey(0)
    # 释放内存
    #cv.destroyAllWindows()
    return label_path

if __name__ == '__main__':
    test_image_path = "data/test/s6/9.pgm"

    result_path = forecast(test_image_path)
    if result_path:
        print(f"标签对应的文件路径: {result_path}")
    else:
        print("未找到对应标签的文件路径")
