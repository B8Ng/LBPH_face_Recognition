import cv2
import train

"""
获取最佳阈值:95
"""


def validate(path, recognizer, threshold):
    faces, ids = train.getImageAndLabels(path)
    correct_predictions = 0
    for face, true_label in zip(faces, ids):
        predicted_label, confidence = recognizer.predict(face)
        if predicted_label == true_label and confidence < threshold:
            correct_predictions += 1
    accuracy = correct_predictions / len(faces)
    return accuracy


if __name__ == '__main__':
    # 训练数据路径
    #train_path = './data/train'
    # 验证数据路径
    validation_path = './data/test'
    #train.train(train_path)
    # 加载训练好的模型
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("trainer/trainer.yml")
    # 通过验证集确定最佳阈值
    accuracies = []
    thresholds = range(110, 120, 2)
    for threshold in thresholds:
        accuracy = validate(validation_path, recognizer, threshold)
        accuracies.append((threshold, accuracy))
    # 找到最佳阈值
    best_threshold, best_accuracy = max(accuracies, key=lambda x: x[1])
    print(f"最佳阈值: {best_threshold}，准确率: {best_accuracy}")
