% Data = rand(90,3);%����ά��Ϊ9��3�������������
function [train_data,test_data] = data_split(Data,comment_len,k)
indices = crossvalind('Kfold', comment_len, k);%��conmmen_len��������������ָ�Ϊk����
for i = 1:k %ѭ��k�Σ��ֱ�ȡ����i������Ϊ��������������k-1������Ϊѵ������
    test = (indices == i);
    train = ~test;
    train_data = Data(train, :);
    test_data = Data(test, :);
end