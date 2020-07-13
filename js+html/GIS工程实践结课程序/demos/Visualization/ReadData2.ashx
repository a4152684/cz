<%@ WebHandler Language="C#" Class="ReadData" %>

using System;
using System.Web;
using System.Text;
using System.Data;
using System.Data.SqlClient;
using System.Collections;
public class ReadData : IHttpHandler
{
    public string deal_Date(string Date)//返回前一天的日期
    {
        string new_Date;
        string[] Date_split = Date.Split('-');
        int month = Convert.ToInt32(Date_split[1]);
        int day = Convert.ToInt32(Date_split[2]);
        if(day==1 && (month==2 || month==4 ||month==6 || month==8 ||month ==9 || month==11))
        {
            day = 31;
            month--;
        }
        else if(day==1 && (month==5 || month==7 ||month==10 || month==12))
        {
            day = 30;
            month--;
        }
        else if(day==1 && month==3)
        {
            day = 29;
            month--;
        }
        else
        {
            day--;
        }

        new_Date = "2020-";
        if(month<10)
        {
            new_Date += "0" + month.ToString() + "-";
        }
        else
        {
            new_Date += month.ToString() + "-";
        }

        if(day<10)
        {
            new_Date += "0" + day.ToString();
        }
        else
        {
            new_Date += day.ToString();
        }

        return new_Date;
    }

    public void ProcessRequest(HttpContext context)
    {
        //POST请求的参数获取
        string type = context.Request.Form["type"];
        string tableName = context.Request.Form["table"];
        string Date = context.Request.Form["date"];
        string Name=context.Request.Form["name"];
        string resulte = "";
        try
        {
            //建立连接对象
            SqlConnection conn = new SqlConnection();
            string dbName = "新冠肺炎疫情数据";
            string p_strUser = "sa";
            string p_strPWD = "a7758258";
            //string ConnectionString = String.Format("Data Source={0};Initial Catalog={1};User ID={2};PWD={3}", "(local)", dbName, p_strUser, p_strPWD);
            string ConnectionString = String.Format("Data Source={0};Initial Catalog={1};User ID={2};PWD={3}", "DESKTOP-3D123F9", dbName, p_strUser, p_strPWD);

            if (type == "select")
            {
                for (int i = 0; i < 3; i++)
                {
                    conn.ConnectionString = ConnectionString;//连接数据库
                    conn.Open();//打开数据库
                    string sql = string.Format("SELECT * FROM {0} WHERE 时间=\'{1}\' AND 省份=\'{2}\'", tableName,Date,Name);//选择查询对应日期和地区的数据
                    SqlCommand cmd = new SqlCommand(sql, conn); //定义一个sql操作命令对象     
                    SqlDataReader Reader = cmd.ExecuteReader(); //执行语句  
                                                                //遍历读取查询结果 
                    while (Reader.Read())
                    {
                        string name = Reader["省份"].ToString();
                        string date = Reader["时间"].ToString();
                        date = date.Split(' ')[0];
                        date = date.Split('/')[1] + "/" + date.Split('/')[2];
                        string confirm = Reader["确诊"].ToString();
                        string heal = Reader["治愈"].ToString();
                        string death = Reader["死亡"].ToString();
                        string new_confirm = Reader["新增确诊"].ToString();
                        resulte += string.Format("{{\"时间\":\"{0}\",\"省份\":\"{1}\"," +
                            "\"累积确诊\":\"{2}\",\"治愈\":\"{3}\",\"死亡\":" +
                            "\"{4}\",\"新增确诊\":\"{5}\"}}",
                            date, name, confirm,heal, death, new_confirm) + ","; //将查询结果拼接成json字符串
                    }
                    cmd = null;
                    Date = deal_Date(Date);//将日期变为前一天
                    conn.Close(); //关闭连接            
                    conn.Dispose(); //释放对象 
                }
            }
        }
        catch (Exception ex)
        {
            throw ex;//抛出异常
        }
        //返回结果到前台
        resulte = "[" + resulte.Remove(resulte.Length - 1, 1) + "]";
        context.Response.ContentType = "text/plain";
        context.Response.Write(resulte != "" ? resulte : "[{}]");

    }

    public bool IsReusable
    {
        get
        {
            return false;
        }
    }

}