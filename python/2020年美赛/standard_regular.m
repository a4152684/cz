function x_out = standard_regular(x_in)
x_max=max(x_in);
x_min=min(x_in);
det_x=x_max-x_min;
for i=1:length(x_in)
    x_out(i)=(x_in(i)-x_min)/det_x;
end
x_out=x_out';