# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 19:25:04 2020

@author: lenovo

"""
import torch as t
from Capcha_pytorch import transform,Captcha,MyNet
from torch.utils.data import DataLoader
import torch.optim as optim
import torch.nn as nn
#from torch.autograd import Variable as V

#设置tensor 网络数据都是在GPU设备上运行
#device = t.device('cuda')
classNum = 26+10
batch_size = 1
acc_best = float('inf')

TRAIN_IMAGE_PATH="../训练/labeled_images/"
TEST_IMAGE_PATH="../测试/captcha_images/"

#数据集实例化
train_dataset=Captcha(TRAIN_IMAGE_PATH,transform,train=True,test=False)
train_loader = DataLoader(dataset=train_dataset, batch_size=batch_size, shuffle=True)

#实例化网络
model = MyNet()
#查看参数个数
# params=list(model.parameters())
 
# k=0
# for i in params:
#     l=1
#     print("该层的结构："+str(list(i.size())))
#     for j in i.size():
#         l*=j
#     print("参数和："+str(l))
#     k=k+1
# print("总参数和："+str(k))

#定义和实例化优化器
optimizer = optim.Adam(model.parameters(), lr=1e-3)

#损失函数
criteon = nn.BCELoss()

#加载模型

#开始训练
for epoch in range(10):        
    model.train()   #必须要写这句
    for batchidx, (x, label) in enumerate(train_loader):
        #x, label = x.to(device), label.to(device)
        logits = model(x)
        loss = criteon(logits, label)        
        # backprop
        optimizer.zero_grad()  #梯度清0
        loss.backward()   #梯度反传
        optimizer.step()   #保留梯度
    print(epoch, 'loss:', loss.item())

#验证和保存模型
val_loader=train_loader

model.eval()    #这句话也是必须的
with t.no_grad():
    total_correct = 0
    total_num = 0
    for x, label in val_loader:
        #x, label = x.to(device), label.to(device)
        logits = model(x)
        pred = logits.argmax(dim=1)
        correct = t.eq(pred, label).float().sum().item()
        total_correct += correct
        total_num += x.size(0)
        print(correct)
        acc = total_correct / total_num
        print(epoch, 'test acc:', acc)

    if acc < acc_best:
        acc_best = acc 
        t.save({'state_dict': model.state_dict(), 'epoch': epoch},'MyNet_'+str(epoch) + '_best.pkl')
        print('Save best statistics done!')

#可视化
viz = visdom.Visdom()
viz.line([0], [-1], win='loss', opts=dict(title='loss'))  #初始化
viz.line([0], [-1], win='val_acc', opts=dict(title='val_acc'))

optimizer.zero_grad()
loss.backward()
optimizer.step()
viz.line([loss.item()], [global_step], win='loss', update='append') #在这里加入loss值

viz.line([val_acc],[global_step], win='val_acc',update='append')