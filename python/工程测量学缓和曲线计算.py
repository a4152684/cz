# -*- coding: utf-8 -*-
"""
Created on Thu May 14 23:35:02 2020

@author: lenovo
"""
import math
pi=math.pi

def compute_a(x1,y1,x2,y2): #x1到x2的方位角
    a=math.atan((y2-y1)/(x2-x1))
    if (x1 < x2) & (y1<y2) :
        return a
    elif (x1<x2) & (y1>y2) :
        return a+2*pi
    else:
        return a+pi


a_d=(46+14/60+52.9/3600);
a_h=a_d*pi/180;
ls=65;
R=360;
KJD6=25582.83;
print("已知条件")
print("圆曲线半径R: "+str(R))
print("缓和曲线长ls: "+str(ls))
print("线路交点JD的里程: "+str(KJD6))
print("偏角a_左: "+str(a_d))
print()

m=ls/2-ls*ls*ls/(240*R*R);
P=ls*ls/(24*R);
b0_h=ls/(2*R);
b0_d=ls*180/(2*R*pi);
print("过渡量")
print("m: "+str(m))
print("P: "+str(P))
print("b_0: "+str(b0_d))
print()

TH=m+(R+P)*math.tan(a_h/2);
LT=R*(a_h-2*b0_h);
LH=R*(a_h-2*b0_h)+2*ls;
EH=(R+P)/(math.cos(a_h/2))-R;
q=2*TH-LH;
print("曲线综合要素")
print("TH: "+str(TH))
print("LT: "+str(LT))
print("LH: "+str(LH))
print("EH: "+str(EH))
print()

KZH=KJD6-TH;
KHY=KZH+ls;
KQZ=KZH+LH/2;
KYH=KHY+LT;
KHZ=KYH+ls;
print("主点里程")
print("KZH: "+str(KZH))
print("KHY: "+str(KHY))
print("KQZ: "+str(KQZ))
print("KYH: "+str(KYH))
print("KHZ: "+str(KHZ))
print("检核：KQZ+1/2q="+str(KQZ+q/2)+", KJD="+str(KJD6))
print()

K1=25700;
#l1=K1-KZH; #左边那个坐标系O‘
l1=KHZ-K1 #右边那个坐标系O''
phi_h1=b0_h+(l1-ls)/R;
#x1=m+R*math.sin(phi_h1);
#y1=P+R*(1-math.cos(phi_h1));圆曲线段的公式
x1=l1-math.pow(l1,5)/(40*R*R*ls*ls)
y1=l1*l1*l1/(6*R*ls) #缓和曲线段的公式
print("计算独立坐标")
print("所求点里程K: "+str(K1))
print("间距l: "+str(l1))
print("角度phi: "+str(phi_h1*180/pi))
print("独立坐标系下,x: "+str(x1)+",y: "+str(y1))
print()

# K2=180;
# l2=K2-KZH;
# phi_h2=b0_h+(l2-ls)/R;
# x2=m+R*math.sin(phi_h2);
# y2=P+R*(1-math.cos(phi_h2));

#XJD1=3162606.831; YJD1=39390001.897;
#XZD1=3162630.051; YZD1=39389768.043;

""" XJD6=389404.665;
YJD6=523201.719;
XJD5=389230.281;
YJD5=523626.411; """
XJD6=398853.1939;
YJD6=540298.0331;
XJD5=399606.2286;
YJD5=539444.3196;
#a_ZH_h=pi+math.atan((YJD6-YJD5)/(XJD6-XJD5));#第一个坐标系O‘下的方位角，即ZH到JD
a_ZH_h=compute_a(XJD5,YJD5,XJD6,YJD6)
#print(a_ZH_h)
a_ZH_h=a_ZH_h-a_h+pi #另一个坐标系O''下的方位角，即HZ到JD，注意左角的话a_h前是减，右角则是加
a_ZH_d=a_ZH_h*180/pi;
print("计算道路方位角")
#print("坐标: "+str(XJD1))
#print("道路方位角aZH: "+str(a_ZH_d))#第一个坐标系O'下
print("道路方位角aHZ: "+str(a_ZH_d))#第二个坐标系O’‘下
print()

XZH=XJD6-TH*math.cos(a_ZH_h);
YZH=YJD6-TH*math.sin(a_ZH_h); #如果是第二个坐标系，此即为HZ坐标
#print("第一个坐标系O’下,计算ZH坐标,XZH: "+str(XZH)+",YZH: "+str(YZH))
print("第二个坐标系O’'下,计算HZ坐标,XHZ: "+str(XZH)+",YHZ: "+str(YZH))

#X1=XZH+math.cos(a_ZH_h)*x1+math.sin(a_ZH_h)*y1;#这是第一个坐标系O'且偏角为左角的情况
#Y1=YZH+math.sin(a_ZH_h)*x1-math.cos(a_ZH_h)*y1;#或者第二个坐标系O''且偏角为右角的情况，即把y前面符号变了下

X1=XZH+math.cos(a_ZH_h)*x1-math.sin(a_ZH_h)*y1  #这是第一个坐标系O‘且偏角为右角的情况
Y1=YZH+math.sin(a_ZH_h)*x1+math.cos(a_ZH_h)*y1  #或者第二个坐标系O''且偏角为左角的情况，即把y前面符号变了下
print("该点在工程坐标系下坐标,X: "+str(X1)+",Y: "+str(Y1))