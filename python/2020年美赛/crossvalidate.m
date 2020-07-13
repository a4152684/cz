function [acc_mean,acc_std]=crossvalidate(sonar,fold,signal)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%sonar is the all data include the class
%fold is the number of crossvalidate
%signal is the signal of classification, if n=0 is decision tree
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

[row column]=size(sonar);
label=sonar(:,column);
classnum=max(label);
start1=1;
for i=1:classnum
    [a,b]=find(label==i);
    datai=sonar(a,:);      %select the i class data 
    [rr1,cc1]=size(datai);
    start1=1;
    %%%%%%%%%part the i class in (fold)%%%%%%%%%%%%%%%%%%%%%
    for j=1:fold-1
        a1=round(length(a)/fold);
        a2=a1-1;
        %fun1=strcat('x*',num2str(a1),'+y*',num2str(a2),'=',num2str(rr1)); 
        %fun2=strcat('x+y=',num2str(fold)); 
        %[x,y]=solve(fun1,fun2) 
        %[x,y] = solve('x*a1+a2*y=rr1','x+y=fold')
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        A=[a1 a2;1 1];
        b=[rr1 fold]';
        x=A\b;
        
        if (j<x(1)+1)
            everynum=a1;
        else
            everynum=a2;
        end
        start2=start1+everynum-1;
       
        eval(['data' num2str(i) num2str(j) '=datai([start1:start2],:);']);
        start1=start2+1;
    end
    eval(['data' num2str(i) num2str(fold) '=datai([start1:length(a)],:);']);
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
for j=1:fold
    eval(['part' num2str(j) '=[];']);
    for i=1:classnum
      eval(['part' num2str(j) '=[part' num2str(j) ';data' num2str(i) num2str(j) '];']);
    end   
end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
accu_m=[];
Samples=[];
Labels=[];
column-1;

for j=1:fold
    Samples=[];
     Labels=[];
     testS=[];
     testL=[];
    for i=1:fold
        
        if (i~=j)
            eval(['Samples=[Samples;part' num2str(i) '(:,1:column-1)];'])
            eval(['Labels=[Labels;part' num2str(i) '(:,column)];'])
        end
    end
    eval(['testS=part' num2str(j) '(:,1:column-1);'])
    eval(['testL=part' num2str(j) '(:,column);'])

    if (signal==0)
       
       t = treefit(Samples,Labels,'method','classification');  % create decision tree
        
       sfit = treeval(t,testS);      % find assigned class numbers      
       ClassRate=length(find((sfit-testL)==0))/length(testL);
       
    end
    accu_m(j)=ClassRate; 
    
end
acc_mean=mean(accu_m);
acc_std=std(accu_m);
accu_m