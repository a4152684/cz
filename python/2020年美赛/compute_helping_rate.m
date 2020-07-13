length=1615;%总评论数
N=sum(helpful_votes)+length;%helpful总人数
dis_votes=total_votes-helpful_votes;%反对的人数

ack=[];
ratio=[];
vi_pur=[];

%读数据
for i=1:length
    if vine(i)=='Y' || vine(i)=='y'
        vi_pur=[vi_pur;1];
    elseif verified_purchase(i)=='Y' || verified_purchase(i)=='y'
        vi_pur=[vi_pur;0.8];
    else
        vi_pur=[vi_pur;0];
    end
    
    if total_votes(i)==0
        ratio=[ratio;1];
    else 
        t=dis_votes(i)/helpful_votes(i);
        if t<=1
            ratio=[ratio;2/(1+t)];
        else
            ratio=[ratio;exp(1-t)];
        end
    end
    
    if helpful_votes(i)>=20
        ack=[ack;1];
    else
        ack=[ack;log(helpful_votes(i)+1)/log(21)];
    end
    
    if helpful_votes(i)>=96 && helpful_votes(i)/total_votes(i)>=0.8
        vi_pur(i)=1;
    elseif helpful_votes(i)>=52 && helpful_votes(i)/total_votes(i)>=0.8
        vi_pur(i)=0.8;
    end
end

%正向化与标准化
ack=standard_regular(ack);
ratio=standard_regular(ratio);
vi_pur=standard_regular(vi_pur);

%灰色关联分析
helping_rate=grey(ack,ratio,vi_pur);