# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 22:38:47 2020

@author: lenovo
"""

import os
try:
    os.mkdir("结果")
except:
    print("结果文件夹已经存在")
finally:
    filename_list=os.listdir("./")
    for filename in filename_list:
        type_name=filename.split('.')[-1]
        if type_name=="txt":
            with open(filename,"r") as f1:
                string=""
                count=1
                f1_list=f1.readlines()
                f1_list.append("\n")
                for line in f1_list:
                    if line!="\n":
                        string+=line
                    else:
                        with open("结果/"+filename[0:-4]+"_"+str(count)+".txt","w") as f2:
                            f2.write(string)
                        string=""
                        count+=1
                