# Study-CSRNet-pytorch

This is the PyTorch version repo for [CSRNet: Dilated Convolutional Neural Networks for Understanding the Highly Congested Scenes](https://arxiv.org/abs/1802.10062) in CVPR 2018, which delivered a state-of-the-art, straightforward and end-to-end architecture for crowd counting tasks.

## 数据集下载
ShanghaiTech Dataset: [Google Drive](https://drive.google.com/open?id=16dhJn7k4FWVwByRsQAEpl9lwjuV03jVI)

## 设备要求

Python: 3.7.1

PyTorch: 1.9.0 

CUDA: cuda10.2

## 获取真值

1.先运行make_dataset.py生成A，B部分的.h文件(在数据集的ground_turth里面，所以要先下载数据集);

## 训练过程

控制台执行python train.py part_A_train.json 0 0 训练A数据集
控制台执行python train.py part_B_train.json 0 0 训练B数据集
训练前记得修改.json下的路径（我是通过记事本一键替换改的数据集所在路径）

## 测试模型

运行val.py可以看到测试模型的正确率（具体需要修改图片路径和训练好的模型路径）

## 查看单个图片或测试模型正确率

运行test_single-image.py，修改路径后可以测试自己想测试的图片。

## pth模型转ONNX模型

运行pth转onnx.py 可以实现模型转换，方便移植到其他深度学习框架。

## Results

ShanghaiA MAE: 66.4 [Google Drive](https://drive.google.com/open?id=1Z-atzS5Y2pOd-nEWqZRVBDMYJDreGWHH)
ShanghaiB MAE: 10.6 [Google Drive](https://drive.google.com/open?id=1zKn6YlLW3Z9ocgPbP99oz7r2nC7_TBXK)

## 引用作者

@inproceedings{li2018csrnet,
  title={CSRNet: Dilated convolutional neural networks for understanding the highly congested scenes},
  author={Li, Yuhong and Zhang, Xiaofan and Chen, Deming},
  booktitle={Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition},
  pages={1091--1100},
  year={2018}

@inproceedings{zhang2016single,
  title={Single-image crowd counting via multi-column convolutional neural network},
  author={Zhang, Yingying and Zhou, Desen and Chen, Siqin and Gao, Shenghua and Ma, Yi},
  booktitle={Proceedings of the IEEE conference on computer vision and pattern recognition},
  pages={589--597},
  year={2016}

