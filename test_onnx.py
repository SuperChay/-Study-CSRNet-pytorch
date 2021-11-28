import cv2
from PIL import Image
from torchvision import transforms

net = cv2.dnn.readNetFromONNX('students.onnx')
image = cv2.imread(r"D:\re2\test_model\test_image\images\IMG_test.jpg")
blob = cv2.dnn.blobFromImage(image)
net.setInput(blob)  # 设置模型输入
out = net.forward()  # 推理出结果
print(out)