length=1615;
comment_score=standard_regular(comment_score);
star_rating=standard_regular(star_rating1);
%x=[star_rating,comment_score];
x=[comment_score,star_rating];
%q=zeros(length,2);
p=zeros(length,2);
for i=1:length
    for j=1:2
        p(i,j)=x(i,j)/sum(x(:,j));
    end
end

k=1/log(length);
s=0;
e=[];
for j=1:2
    for i=1:length
        if p(i,j)==0
            continue
        end
        s=s-k*sum(p(i,j).*log(p(i,j)));
    end
    e=[e;s];
    s=0;
end

d=1-e;
w=[];
for j=1:2
    w=[w;d(j)/sum(d)];
end


score=x*w;