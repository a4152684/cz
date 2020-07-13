# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 12:52:55 2020

@author: lenovo
"""

from Capcha_pytorch import img2list,MyNet,Captcha,transform
import torch as t
from torch.utils.data import DataLoader

TEST_FILE_PATH="../测试/captcha_images/"
CKPT_PATH="./MyNet_9_best.pkl"

model=MyNet()

#加载模型
checkpoints = t.load(CKPT_PATH)  #是字典型，包含训练次数等
checkpoint = checkpoints['state_dict']
step = checkpoints['epoch']   #训练的批次
model.load_state_dict(checkpoint)
print("=> loaded checkpoint: %s"%CKPT_PATH)

test_dataset=Captcha(TEST_FILE_PATH,transform,train=False,test=True)
test_loader = DataLoader(dataset=test_dataset, batch_size=1, shuffle=True)