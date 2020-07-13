% Data = rand(90,3);%创建维度为9×3的随机矩阵样本
function [train_data,test_data] = data_split(Data,comment_len,k)
indices = crossvalind('Kfold', comment_len, k);%将conmmen_len个数据样本随机分割为k部分
for i = 1:k %循环k次，分别取出第i部分作为测试样本，其余k-1部分作为训练样本
    test = (indices == i);
    train = ~test;
    train_data = Data(train, :);
    test_data = Data(test, :);
end