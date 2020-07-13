comment_len=358;
dic_words_len=162;
B=zeros(comment_len,dic_words_len);
fid=fopen('kkknew.txt');  %打开文本文件
fid2=fopen('flagnew.txt');
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

comment_score_y=B*x;
comment_score=2*comment_score_y+3;
comment_predict_star=round(comment_score);
for i=1:length(comment_predict_star)
    if comment_predict_star(i)>5
        comment_predict_star(i)=5;
    end
    if comment_predict_star(i)<1
        comment_predict_star(i)=1;
    end
end