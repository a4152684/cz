comment_len=32024;
dic_words_len=5163;
B=zeros(comment_len,dic_words_len);
fid=fopen('kkk.txt');  %打开文本文件
fid2=fopen('flag.txt');
while ~feof(fid)
   str = fgetl(fid);   % 读取一行, str是字符串c
   str2=fgetl(fid2);
   s=strsplit(str,',');   % 找出str中的空格, 以空格作为分割数据的字符
   s2=strsplit(str2,',');
   for j=1:comment_len-1
       for i=2:length(s)-1
           k=str2num(cell2mat(s(i)));
           k2=str2num(cell2mat(s2(i)));
           if k2==-1
                B(j,k)=B(j,k)-1;
           else
                B(j,k)=B(j,k)+1;
           end
       end
   str = fgetl(fid);   % 读取一行, str是字符串
   str2=fgetl(fid2);
   s=strsplit(str,',');   % 找出str中的空格, 以空格作为分割数据的字符
   s2=strsplit(str2,',');
   end
end

fclose(fid);
fclose(fid2);

y=star_rating/2-1.5;
Data=[B,y];
[train_data,test_data] = data_split(Data,comment_len,10); %划分为9：1的训练集和测试集

% sumk=[]
% for lambta=1:100
%     [x,stauts]=l1_ls(B,y,lambta);
%     sumk=[sumk,(y-B*x)'*(y-B*x)]%+lambta*sum(abs(x))]
% end

train_y=train_data(:,dic_words_len+1);
train_B=train_data(:,1:dic_words_len);
test_y=test_data(:,dic_words_len+1);
test_B=test_data(:,1:dic_words_len);

lambta=100;
[x,stauts]=l1_ls(train_B,train_y,lambta);

%在训练集上的准确率
train_y_predict=train_B*x;
train_star_predict=train_y_predict*2+3;
train_star_predict=round(train_star_predict);
train_v=train_star_predict-(2*train_y+3);

%在测试集上的准确率
test_y_predict=test_B*x;
test_star_predict=test_y_predict*2+3;
test_star_predict=round(test_star_predict);
test_v=test_star_predict-(2*test_y+3);

%t检验
NBB=B'*B;
Q=inv(NBB);
sigma=sqrt(train_v'*train_v/(comment_len-dic_words_len));
%显著性水平a=0.05，个数可看为无穷
t_a=1.96;
t_list=[];
for i=1:dic_words_len
    t=x(i)/(sigma*sqrt(Q(i,i)));
    if abs(t)<t_a
        x(i)=0;
    end
    t_list=[t_list,t];
end
