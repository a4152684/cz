# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 10:32:30 2020

@author: lenovo
"""

import torch as t
#import matplotlib.pyplot as plt
#t.manual_seed(1000)
from PIL import Image
from torchvision.transforms import ToTensor,ToPILImage
from torch import nn
from torch.autograd import Variable as V

def get_fake_data(batch_size=8):
    x=t.rand(batch_size,1)*20
    y=x*2+(1+t.randn(batch_size,1))*3
    return x,y

def clearNoise(image, N=3, Z=5): # 去噪
    img=Image.new("1",image.size)#模式“1”为二值图像，非黑即白。
    draw = ImageDraw.Draw(img)
    for i in range(0, Z):
        draw.point((0, 0), 0)
        draw.point((image.size[0] - 1, image.size[1] - 1),1) #两个端点都赋值

        for x in range(1, image.size[0] - 1):
            for y in range(1, image.size[1] - 1):
                nearDots = 0
                L = image.getpixel((x,y))
                if L == image.getpixel((x-1,y-1)):
                    nearDots += 1
                if L == image.getpixel((x-1,y)):
                    nearDots += 1
                if L == image.getpixel((x-1,y+1)):
                    nearDots += 1
                if L == image.getpixel((x,y-1)):
                    nearDots += 1
                if L == image.getpixel((x,y+1)):
                    nearDots += 1
                if L == image.getpixel((x+1,y-1)):
                    nearDots += 1
                if L == image.getpixel((x+1,y)):
                    nearDots += 1
                if L == image.getpixel((x+1,y+1)):
                    nearDots += 1

                if nearDots < N:
                     draw.point((x, y), 1)#若邻域内与其相等的像素个数很少，则认为是空白点
    return img

if __name__ == "__main__":
    to_tensor=ToTensor()
    to_pil=ToPILImage()
    img=Image.open('Lena.jpg')
    img = img.convert('L') #灰度化
    
    input=to_tensor(img).unsqueeze(0)
    
    #卷积
    kernel=t.ones(3,3)/-9
    kernel[1][1]=1
    conv=nn.Conv2d(1,1,(3,3),1,bias=False)
    conv.weight.data=kernel.view(1,1,3,3)
    
    out_conv=conv(V(input))
    out_conv_img=to_pil(out_conv.data.squeeze(0))
    
    #池化
    pool=nn.AvgPool2d(2,2)
    list(pool.parameters())
    out_pool=pool(V(input))
    out_pool_img=to_pil(out_pool.data.squeeze(0))
    
    input2=V(t.randn(2,3))
    linear=nn.Linear(3,4)
    h=linear(input2)