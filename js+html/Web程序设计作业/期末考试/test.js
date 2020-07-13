// JavaScript Document
function first()
{
	if(document.getElementById("DH").style.display=="none")
		{
			document.getElementById("DH").style.display = "block";
			document.getElementById("b1").value="隐藏图片";
		}
	else{
		document.getElementById("DH").style.display = "none";
			document.getElementById("b1").value="显示图片";
	}
	
}

function two1_in()
{
	document.getElementById("1").bgColor="#FFFFFF";
	document.getElementById("111").color="#000000";
	document.getElementById("text").value="1月活动内容";	
}

function two1_out()
{
	document.getElementById("1").bgColor="#000000";
	document.getElementById("111").color="#FFFFFF";
	document.getElementById("text").value="";
}

function two2_in()
{
	document.getElementById("2").bgColor="#FFFFFF";
	document.getElementById("222").color="#000000";
	document.getElementById("text").value="2月活动内容";
}

function two2_out()
{
	document.getElementById("2").bgColor="#000000";
	document.getElementById("222").color="#FFFFFF";
	document.getElementById("text").value="";
}

function two3_in()
{
	document.getElementById("3").bgColor="#FFFFFF";
	document.getElementById("333").color="#000000";
	document.getElementById("text").value="3月活动内容";
}

function two3_out()
{
	document.getElementById("3").bgColor="#000000";
	document.getElementById("333").color="#FFFFFF";
	document.getElementById("text").value="";
}

function two4_in()
{
	document.getElementById("4").bgColor="#FFFFFF";
	document.getElementById("444").color="#000000";
	document.getElementById("text").value="4月活动内容";
}

function two4_out()
{
	document.getElementById("4").bgColor="#000000";
	document.getElementById("444").color="#FFFFFF";
	document.getElementById("text").value="";
}

function two5_in()
{
	document.getElementById("5").bgColor="#FFFFFF";
	document.getElementById("555").color="#000000";
	document.getElementById("text").value="5月活动内容";
}

function two5_out()
{
	document.getElementById("5").bgColor="#000000";
	document.getElementById("555").color="#FFFFFF";
	document.getElementById("text").value="";
}

function two6_in()
{
	document.getElementById("6").bgColor="#FFFFFF";
	document.getElementById("666").color="#000000";
	document.getElementById("text").value="6月活动内容";
}

function two6_out()
{
	document.getElementById("6").bgColor="#000000";
	document.getElementById("666").color="#FFFFFF";
	document.getElementById("text").value="";
}

function two7_in()
{
	document.getElementById("7").bgColor="#FFFFFF";
	document.getElementById("777").color="#000000";
	document.getElementById("text").value="7月活动内容";
}

function two7_out()
{
	document.getElementById("7").bgColor="#000000";
	document.getElementById("777").color="#FFFFFF";
	document.getElementById("text").value="";
}

function two8_in()
{
	document.getElementById("8").bgColor="#FFFFFF";
	document.getElementById("888").color="#000000";
	document.getElementById("text").value="8月活动内容";
}

function two8_out()
{
	document.getElementById("8").bgColor="#000000";
	document.getElementById("888").color="#FFFFFF";
	document.getElementById("text").value="";
}

function two9_in()
{
	document.getElementById("9").bgColor="#FFFFFF";
	document.getElementById("999").color="#000000";
	document.getElementById("text").value="9月活动内容";
}

function two9_out()
{
	document.getElementById("9").bgColor="#000000";
	document.getElementById("999").color="#FFFFFF";
	document.getElementById("text").value="";
}

function two10_in()
{
	document.getElementById("10").bgColor="#FFFFFF";
	document.getElementById("1010").color="#000000";
	document.getElementById("text").value="10月活动内容";
}

function two10_out()
{
	document.getElementById("10").bgColor="#000000";
	document.getElementById("1010").color="#FFFFFF";
	document.getElementById("text").value="";
}

function two11_in()
{
	document.getElementById("11").bgColor="#FFFFFF";
	document.getElementById("1111").color="#000000";
	document.getElementById("text").value="11月活动内容";
}

function two11_out()
{
	document.getElementById("11").bgColor="#000000";
	document.getElementById("1111").color="#FFFFFF";
	document.getElementById("text").value="";
}

function two12_in()
{
	document.getElementById("12").bgColor="#FFFFFF";
	document.getElementById("1212").color="#000000";
	document.getElementById("text").value="12月活动内容";
}

function two12_out()
{
	document.getElementById("12").bgColor="#000000";
	document.getElementById("1212").color="#FFFFFF";
	document.getElementById("text").value="";
}

function third()
{	var str="";
 
	var name=document.getElementById("xm").value;
	str=str+name+"\n";
 
	var age=document.getElementById("nl").value;
	str=str+age+"\n";
 
 	var sex;
 	if(document.getElementById("nan").checked)
	   {
	   		sex="男";
	   }
	   else {
	   		sex="女";
	   }
	str=str+sex+"\n";
	
 	var zjlx=document.getElementById("zjlx");
 	str=str+zjlx.value;
	var zjhm=document.getElementById("zjhm").value;
	str=str+"编号:"+zjhm+"\n";
 
 	var jtzz=document.getElementById("jtzz").value;
	str=str+jtzz+"\n";
 
 	var lxdh=document.getElementById("lxdh").value;
	str=str+lxdh+"\n";
 
 	var email=document.getElementById("email").value;
	str=str+email+"\n";
 
 	if(document.getElementById("yd").checked)
		{
			str=str+"运动 ";
		}
 	if(document.getElementById("dy").checked)
		{
			str=str+"钓鱼 ";
		}
 	if(document.getElementById("wlyx").checked)
		{
			str=str+"网络游戏";
		}
 	str=str+"\n";
 
 	var yj=document.getElementById("yj").value;
	str=str+yj+"\n";
 
	alert(str);
}

function third_2()
{
	document.getElementById("xm").value="";
	document.getElementById("nl").value="";
	document.getElementById("zjhm").value="";
	document.getElementById("jtzz").value="";
	document.getElementById("lxdh").value="";
	document.getElementById("email").value="";
	document.getElementById("yj").value="";
}


