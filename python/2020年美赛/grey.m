function helping_rate = grey(x1,x2,x3)
x_max=[];
for i = 1:length(x1)
    x_max=[x_max; max([x1(i),x2(i),x3(i)])];%Ä¸ÐòÁÐ
end

% global min and max
global_min  = min(min(abs([x1; x2; x3] - repmat(x_max, [3, 1]))));
global_max = max(max(abs([x1; x2; x3] - repmat(x_max, [3, 1]))));

% set rho
rho = 0.5;

% calculate zeta relation coefficients
zeta_1 = (global_min + rho * global_max) ./ (abs(x_max - x1) + rho * global_max);
zeta_2 = (global_min + rho * global_max) ./ (abs(x_max - x2) + rho * global_max);
zeta_3 = (global_min + rho * global_max) ./ (abs(x_max - x3) + rho * global_max);
% zeta_4 = (global_min + rho * global_max) ./ (abs(x_max - x4) + rho * global_max);

r=[sum(zeta_1),sum(zeta_2),sum(zeta_3)];
w=[r(1),r(2),r(3)]/sum(r);

score=x1*r(1)+x2*r(2)+x3*r(3);

%helping_rate=score;%/sum(score);
helping_rate=standard_regular(score);

