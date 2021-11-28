import h5py
import scipy.io as io
import PIL.Image as Image
import numpy as np
import os
import glob
from matplotlib import pyplot as plt
from scipy.ndimage.filters import gaussian_filter
import scipy
import json
import torchvision.transforms.functional as F
from matplotlib import cm as CM
from image import *
from model import CSRNet
import torch
from matplotlib import cm as c

from torchvision import datasets, transforms

transform=transforms.Compose([
                       transforms.ToTensor(),transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                     std=[0.229, 0.224, 0.225]),
                   ])

model = CSRNet()

#defining the model

model = model.cuda()

#loading the trained weights

checkpoint = torch.load(R"C:\Users\36432\Desktop\PartBmodel_best.pth.tar")

model.load_state_dict(checkpoint['state_dict'])
dummy_input = torch.randn(1, 3, 256, 256, device='cuda:0')
torch.onnx._export(model, dummy_input, "student_A.onnx", verbose=True, opset_version=11)
