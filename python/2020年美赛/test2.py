# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 17:34:52 2020

@author: lenovo
"""
import operator
import nltk
import re

stop_words_file='stop_words.txt'
#with open(english,'r',encoding='utf-8') as file:
#    u=file.read()

list_word_result=[]
#for i in range(1,4):
#    english='body'+str(i)+'.txt'
#    f1=open(english,'r',encoding='utf-8')
#    u=f1.readline()
#    while u!='' :
#        string=re.sub('[^\w ]','',u)
#        string=string.lower()#小写
#        list_word_result.append(nltk.word_tokenize(string))
#        u=f1.readline()
#    #print(nltk.pos_tag(nltk.word_tokenize(str))) #对分完词的结果进行词性标注
#    f1.close()

f1=open('all_review.txt','r',encoding='utf-8')
u=f1.readline()
while u!='' :
    string=re.sub('[^\w ]','',u)
    string=string.lower()#小写
    list_word_result.append(nltk.word_tokenize(string))
    u=f1.readline()
#print(nltk.pos_tag(nltk.word_tokenize(str))) #对分完词的结果进行词性标注
f1.close()

#停用词添加
#stop_words=[]
#f2=open(stop_words_file,'r',encoding='utf-8')
#sr=f2.readline().rstrip("\n")
#while sr!='' :
#    stop_words.append(sr)
#    sr=f2.readline().rstrip("\n")
#f2.close()


# 利用字典进行处理
dic = {}
for wordlist in list_word_result:
    for word in wordlist:
#        if word in stop_words:#停止词则跳过
#            continue
        if word not in dic:
            dic[word] = 1
        else:
            dic[word] = dic[word] + 1
swd=sorted(dic.items(), key=operator.itemgetter(1),reverse=True)#排序
#输出前100个频数单词
count=0
for sw in swd:
    print(sw)
    count+=1
    if count>=100:
        break
#
##将有的词写成文档
#f3=open('words.txt','w',encoding='utf-8')
#for word in dic.keys():
#    f3.writelines(word+'\n')
#f3.close()
#
##将有的频数写成文档d
#f4=open('frequency.txt','w',encoding='utf-8')
#for frequency in dic.values():
#    f4.writelines(str(frequency)+'\n')
#f4.close()
#
#将有的频数写成文档
f5=open('all_items.txt','w',encoding='utf-8')
for word,frequency in dic.items():
    f5.writelines(word+','+str(frequency)+'\n')
f5.close()

