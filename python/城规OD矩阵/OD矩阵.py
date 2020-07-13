import pandas as pd
'''原始数据'''
row=3#行
col=3#列
OD_origin=[[5,7,4],[7,10,6],[4,5,15]]#基准OD矩阵
O_predict=[40,90,36] #预测值Oi
D_predict=[40,90,36] #预测值Dj
result_filename="E:\曹臻个人\专业课\城市规划原理\OD矩阵\OD矩阵结果.xlsx"

""" OD_origin=[[17,7,4],[7,38,6],[4,5,17]]#基准OD矩阵
O_predict=[38.6,91.9,36.0] #预测值Oi
D_predict=[39.3,90.3,36.9] #预测值Dj
result_filename="E:\曹臻个人\专业课\城市规划原理\OD矩阵\OD矩阵结果.xlsx" """

M=10 #最大迭代次数
e=0.01 #阈值

def f(Foi,Fdj):
    return (Foi+Fdj)/2 #平均增长率法
    #return() #常增长率法

'''计算部分'''
#转置
def Transpose(OD): 
    OD_T=[ [0 for i in range(row)] for j in range(col)]
    for i in range(col):
        for j in range(row):
            OD_T[j][i]=OD[i][j]
    return OD_T

OD=OD_origin
first=[j+1 for j in range(row)]
first.append('Dj')
df=[]
Oi=[sum(OD[j]) for j in range(col)]
df.append({'O\D': first+["吸收增长系数"], 
            '1': Transpose(OD)[0]+[sum(Transpose(OD)[0])]+[D_predict[0]/sum(Transpose(OD)[0])], 
            '2': Transpose(OD)[1]+[sum(Transpose(OD)[1])]+[D_predict[1]/sum(Transpose(OD)[1])], 
            '3': Transpose(OD)[2]+[sum(Transpose(OD)[2])]+[D_predict[2]/sum(Transpose(OD)[2])], 
            'Oi': Oi+[sum(Oi),''], 
            '预测值Oi':O_predict+[sum(O_predict),''],
            "发生增长系数":[O_predict[j]/Oi[j] for j in range(row)] + ['','']})

for i in range(M):
    O=[sum(OD[j]) for j in range(col)]
    D=[sum(Transpose(OD)[j]) for j in range(row)]
    Fo=[O_predict[j]/O[j] for j in range(row)]
    Fd=[D_predict[j]/D[j] for j in range(col)]
    
    OD_T=[ [0 for i in range(row)] for j in range(col)]
    for j in range(row):
        for k in range(col):
            OD_T[j][k]=OD[j][k]*f(Fo[j],Fd[k])
    OD=OD_T   
    
    Oi=[sum(OD[j]) for j in range(col)]
    df.append({'O\D': first+["吸收增长系数"], 
              '1': Transpose(OD)[0]+[sum(Transpose(OD)[0])]+[D_predict[0]/sum(Transpose(OD)[0])], 
              '2': Transpose(OD)[1]+[sum(Transpose(OD)[1])]+[D_predict[1]/sum(Transpose(OD)[1])], 
              '3': Transpose(OD)[2]+[sum(Transpose(OD)[2])]+[D_predict[2]/sum(Transpose(OD)[2])], 
              'Oi': Oi+[sum(Oi),''], 
              '预测值Oi':O_predict+[sum(O_predict),''],
              "发生增长系数":[O_predict[j]/Oi[j] for j in range(row)] + ['','']})

    if abs(max((max(Fo)),max(Fd))-1)<e: #阈值
        break

'''写入部分'''    
writer = pd.ExcelWriter(result_filename)
for i in range(len(df)):
    df2 = pd.DataFrame(df[i])
    df2.to_excel(writer, "第"+str(i)+"次迭代",index=None)
writer.save()
print("end")


