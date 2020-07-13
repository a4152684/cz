# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 21:30:03 2020

@author: lenovo
"""
import nltk
import re

privative_words_list=['not','no','never','dont','doesnt']

effective_words=[]
f1=open('effective_words.txt','r',encoding='utf-8')
sr=f1.readline().rstrip("\n")
while sr!='' :
    effective_words.append(sr)
    sr=f1.readline().rstrip("\n")
f1.close()

effective_words_len=len(effective_words)
index=0
f1=open('new_body.txt','r',encoding='utf-8')
f2=open('kkknew.txt','w',encoding='utf-8')
f3=open('flagnew.txt','w',encoding='utf-8')
count=0
flag=''
u=f1.readline()
while u!='' :
    string=re.sub('[^\w ]','',u)#正则化
    string=string.lower()#小写
    number=[count]
    flags=[count]
    
    for word in nltk.word_tokenize(string):#每句话
        if word in effective_words:
            index=effective_words.index(word)
            number.append(index)   
            if flag in privative_words_list:
                flags.append(-1)
            else:
                flags.append(1)
        flag=word#如果前一个词flag是'not'则分数为负
    count+=1
    
    for i in number:
        f2.write(str(i)+',')
    f2.write('\n')
    
    for i in flags:
        f3.write(str(i)+',')
    f3.write('\n')
    u=f1.readline()
#print(nltk.pos_tag(nltk.word_tokenize(str))) #对分完词的结果进行词性标注
f1.close()
f2.close()
f3.close()