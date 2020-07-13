// JavaScript Document
function first()
{
	var x=Number(document.form.text1.value);
	var y=Number(document.form.text2.value);
	var z;
	var select = document.getElementById('select');
    var index = select.selectedIndex;
    flag = select.options[index].value;
	if(flag=="jia") z=x+y;
	else if(flag=="jian") z=x-y;
	else if(flag=="cheng") z=x*y;
	else  z=x/y;
	document.form.text3.value=z;
}

function DHover()
{
	document.getElementById("DH").style.display = "block";
}

function DHout()
{
	document.getElementById("DH").style.display = "none";
}

function GYSover()
{
	document.getElementById("GYS").style.display = "block";
}

function GYSout()
{
	document.getElementById("GYS").style.display = "none";
}

function HLover()
{
	document.getElementById("HL").style.display = "block";
}

function HLout()
{
	document.getElementById("HL").style.display = "none";
}