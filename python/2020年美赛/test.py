# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 17:15:56 2020

@author: lenovo
"""

# -*- coding: utf-8 -*-
 
import pandas as pd
import jieba
from nltk.stem import WordNetLemmatizer
 
 
"""
函数说明：简单分词
Parameters:
     filename:数据文件
Returns:
     list_word_split：分词后的数据集列表
     category_labels: 文本标签列表
"""
def word_split(filename):
    read_data=pd.read_excel(filename)
    list_word_split=[]
    category_labels=[]
    for i in range(len(read_data)):
        row_data = read_data.iloc[i, 1]           # 读取单个漏洞描述文本
        list_row_data = list(jieba.cut(row_data)) # 对单个漏洞进行分词
        list_row_data=[x for x in list_row_data if x!=' '] #去除列表中的空格字符
        list_word_split.append(list_row_data)
 
        row_data_label=read_data.iloc[i,2]   #读取单个漏洞的类别标签
        category_labels.append(row_data_label) #将单个漏洞的类别标签加入列表
    return list_word_split, category_labels
 
 
"""
函数说明：词性还原
Parameters:
     list_words:数据列表
Returns:
     list_words_lemmatizer：词性还原后的数据集列表
"""
def word_lemmatizer(list_words):
    wordnet_lemmatizer = WordNetLemmatizer()
    list_words_lemmatizer = []
    for word_list in list_words:
        lemmatizer_word = []
        for i in word_list:
            lemmatizer_word.append(wordnet_lemmatizer.lemmatize(i))
        list_words_lemmatizer.append(lemmatizer_word)
    return list_words_lemmatizer
 
 
"""
函数说明：停用词过滤
Parameters:
     filename:停用词文件
     list_words_lemmatizer:词列表
Returns:
     list_filter_stopwords：停用词过滤后的词列表
"""
def stopwords_filter(filename,list_words_lemmatizer):
    list_filter_stopwords=[]  #声明一个停用词过滤后的词列表
    with open(filename,'r') as fr:
        stop_words=list(fr.read().split('\n')) #将停用词读取到列表里
        for i in range(len(list_words_lemmatizer)):
            word_list = []
            for j in list_words_lemmatizer[i]:
                if j not in stop_words:
                    word_list.append(j.lower()) #将词变为小写加入词列表
            list_filter_stopwords.append(word_list)
        return list_filter_stopwords
 
if __name__=='__main__':
    # 加载自定义词库
    jieba.load_userdict(r'./all_words.txt')

    # 读入停止词
   # with open(r'./stop_words_eng.txt') as words:
        #stop_words = [i.strip() for i in words.readlines()]
    
    list_word_split, category_labels=word_split('testdata.xls') #获得每条文本的分词列表和标签列表
    print('分词成功')
    list_words_lemmatizer=word_lemmatizer(list_word_split)  #词性还原
    print('词性还原成功')
    list_filter_stopwords=stopwords_filter('stopwords.txt',list_words_lemmatizer) #获得停用词过滤后的列表
    print("停用词过滤成功")
