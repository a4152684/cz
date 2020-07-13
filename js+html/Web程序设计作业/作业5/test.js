// JavaScript Document
function IsPrime(num)
{
	var flag=true;//true表明是素数
	if(num<2) flag=false;
	for(var i=2;i<num/2; i++)
		{
			if(num%i==0)
				{
					flag=false;
					break;
				}
		}
	return flag;
}

function F(n)
{
	if(n==1 || n==2) return 1;
	else return F(n-1)+F(n-2);
}