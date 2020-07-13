headline_len=1615;
dic_words_len=191;
B=zeros(headline_len,dic_words_len);
fid=fopen('kkh3.txt');  %打开文本文件
fid2=fopen('flagh3.txt');
while ~feof(fid)
   str = fgetl(fid);   % 读取一行, str是字符串c
   str2=fgetl(fid2);
   s=strsplit(str,',');   % 找出str中的空格, 以空格作为分割数据的字符
   s2=strsplit(str2,',');
   for j=1:headline_len-1
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

headline_score_y=B*x;
headline_score=2*headline_score_y+3;
headline_predict_star=round(headline_score);
for i=1:length(headline_predict_star)
    if headline_predict_star(i)>5
        headline_predict_star(i)=5;
    end
    if headline_predict_star(i)<1
        headline_predict_star(i)=1;
    end
end