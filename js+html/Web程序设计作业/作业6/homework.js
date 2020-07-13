// JavaScript Document
function first(){
	document.form.textfield2.value=document.form.textfield1.value;
}

function second(){
	var x=document.getElementsByName("RadioGroup1");
	for(var i=0;i<x.length;i++)
		{
			if(x[i].checked)
				{
					break;
				}
		}
	switch(i){
		case 0: window.open("https://news.qq.com"); break;
        case 1: window.open("https://www.sina.com.cn"); break;
        case 2: window.open("https://www.sohu.com"); break;
        case 3: window.open("http://www.ifeng.com"); break;	
	}
}

var timer;
function third1(){
	timer=window.setInterval(third3,50);
}

function third2(){
	window.clearInterval(timer);
	alert("中奖号码"+document.form.text1.value);
}

function third3(){
	document.form.text1.value=Math.floor(Math.random()*100+1);
}

function fourth1(){
	timer=window.setInterval(fourth2,1000);
}

function fourth2(){
	document.body.innerHTML="";
	var date = new Date();
    var year = date.getFullYear();
    var month = date.getMonth()+1;
    var day = date.getDate();
    var hour = date.getHours();
    var minutes = date.getMinutes();
    var seconds = date.getSeconds();
	var id = date.getDay();
    var weekends=['星期日','星期一','星期二','星期三',
                     '星期四','星期五','星期六'];
	var s="<font color='blue'>";
	if(hour>0 && hour<12)
		{
			s=s+"早上好！";
		}
	else if(hour>=12 && hour<18)
		{
			s=s+"中午好！";
		}
	else
		{
			s=s+"晚上好！";
		}
	s=s+"</font> <br>";
	s=s+"当前日期：<font color='blue'>"+year+"年"+month+"月"
	+day+"日 "+weekends[id];
	s=s+"</font> <br>";
	s=s+"当前时间：<font color='blue'>"+hour+":"+minutes+":"+seconds;
	s=s+"</font> <br>";
	document.write(s);
}