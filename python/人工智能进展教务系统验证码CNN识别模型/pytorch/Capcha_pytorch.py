# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 23:17:47 2020

@author: lenovo
"""

from PIL import Image,ImageDraw
#import os
from torch.utils import data
import numpy as np
from torchvision import transforms as T
import queue
from imutils import paths
import torch.nn as nn
import torch.nn.functional as F
import torch as t
#from torchvision.transforms import ToTensor,ToPILImage

def twoValue(image,G=127):#阈值为G的二值化
    img=Image.new("1",image.size)#模式“1”为二值图像，非黑即白。
    draw = ImageDraw.Draw(img)
    for y in range(0, image.size[1]):
        for x in range(0, image.size[0]):
            g = image.getpixel((x, y))
            if g > G:
                draw.point((x, y), 1)
            else:
                draw.point((x, y), 0)#小于阈值则视作黑色点
    return img

def cfs(img):#img此时已经经过去噪，二值化
    """传入二值化后的图片进行连通域分割"""
    pixdata = img.load()#方法load()返回一个用于读取和修改像素的像素访问对象,这个访问对象像一个二维队列
    w,h = img.size
    visited = set() #创建一个集合
    q = queue.Queue() #单向队列，先进先出
    offset = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]
    x_cuts = []
    y_cuts = []
    for x in range(w):
        for y in range(h):
            x_axis = []
            y_axis = []
            if pixdata[x,y] == 0 and (x,y) not in visited:
                q.put((x,y))#如果(x,y)处像素值为0且其没有被访问过(即不在集合visited中)
                visited.add((x,y))#则将其放入队列q，并且设置为访问过
            while not q.empty():#当队列不空的时候
                x_p,y_p = q.get()#取出最先进入的一个
                for x_offset,y_offset in offset:
                    x_c,y_c = x_p+x_offset,y_p+y_offset
                    if (x_c,y_c) in visited:
                        continue
                    visited.add((x_c,y_c))
                    try:
                        if pixdata[x_c,y_c] == 0:
                            q.put((x_c,y_c))
                            x_axis.append(x_c)
                            y_axis.append(y_c)
                            #y_axis.append(y_c)
                    except:
                        pass
            if x_axis:
                min_x,max_x = min(x_axis),max(x_axis)
                min_y,max_y = min(y_axis),max(y_axis)
                if max_x - min_x >  3:
                    # 宽度小于3的认为是噪点，根据需要修改
                    x_cuts.append((min_x,max_x + 1))
                    y_cuts.append((min_y,max_y + 1))
    return x_cuts,y_cuts

def img2list(image):
    image=twoValue(image)#设置阈值，并二值化
    #clearNoise(image, 1, 1)#去除噪声
    #image=saveImage(image.size)#将原图片用已经去噪和二值化的图片覆盖
    x_cuts,y_cuts=cfs(image)#二值化图像分割
    image_list=[]
    
    for j, item in enumerate(x_cuts): #j为列表索引，item为j对应的值
        if j<4:
            box = (item[0], 0, item[1], 30)#(left, upper, right, lower)，本图片中字母高度不变
            image_list.append(image.crop(box))
            
    return image_list

transform=T.Compose([
    T.Resize(128),#缩放图片
    T.CenterCrop(128),#至128*128,或者T.Resize([128,128])
    T.ToTensor()
    ])

def label_trans(label):
    new_list=[0 for x in range(0,36)]
    n=ord(label)
    if n>=ord('0') and n<=ord('9'):
        new_list[n-ord('0')]=1
    elif n>=ord('a') and n<=ord('z'):
        new_list[n-ord('a')+10]=1
    return new_list
    
    
class Captcha(data.Dataset):
    def __init__(self,root,transforms=None,train=True,test=False):
        self.img_paths=[]
        self.transforms=transforms
        self.test=test
        self.train=train
        
        for filename in list(paths.list_images(root)):
            self.img_paths.append(filename)
            
        self.img_num=len(self.img_paths)
        
        #划分训练，验证集       
    
    def __getitem__(self,index):#获取的是文件名而不是一次性将图片读入内存
            img_path=self.img_paths[index]
            label = (img_path.split("\\")[0]).split("/")[-1] #os.path.sep路径分隔符，一般是"/"
            data=Image.open(img_path)
            if self.transforms:
                data=self.transforms(data)
            label=label_trans(label)
            #label=np.array(label)
            label=t.FloatTensor(label)
            #label.dtype='float32'
            return data,label

    def __len__(self):
        return self.img_num
    
class MyNet(nn.Module):
    def __init__(self):
        super(MyNet, self).__init__()
        #定义class torch.nn.Conv2d
        #(in_channels, out_channels, kernel_size, stride=1, padding=0, dilation=1, groups=1, bias=True)
        self.conv1=nn.Conv2d(1,1,(3,3))
        self.conv2=nn.Conv2d(1,1,(3,3))
        
        #全连接函数，将32*32个节点连接到256个节点上
        self.fc1=nn.Linear(30*30,256)
        self.fc2=nn.Linear(256,84)
        self.fc3=nn.Linear(84,36)
        
    #定义神经网络的前向传播，一旦定义成功，那么后向传播也会自动生成（autograd）
    def forward(self, x):
        #输入的x经过卷积conv1之后，经过relu激活函数，再通过2*2的窗口进行最大池化
        x=F.max_pool2d(F.relu(self.conv1(x)),(2,2))
        x=F.max_pool2d(F.relu(self.conv2(x)),(2,2))
        #view函数将张量x变形为一维向量的形式，总特征数不变，为接下来的全连接做准备
        x=x.view(-1,30*30) 
        
        #输入x,经过全连接1层再经过relu函数,然后更新x
        x=F.relu(self.fc1(x))
        x=F.relu(self.fc2(x))
        x=nn.sigmoid(self.fc3(x))
        return x
    
if __name__ == "__main__":
    TRAIN_IMAGE_PATH="../训练/labeled_images/"
    TEST_IMAGE_PATH="../测试/captcha_images/"
    dataset=Captcha(TRAIN_IMAGE_PATH,transform)
    for img,label in dataset:
        print(img.size,label)
    
    
    
    