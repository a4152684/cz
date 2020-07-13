<%@ WebHandler Language="C#" Class="ReadData" %>

using System;
using System.Web;
using System.Text;
using System.Data;
using System.Data.SqlClient;
using System.Collections;
public class ReadData : IHttpHandler
{

    public void ProcessRequest(HttpContext context)
    {
        //POST请求的参数获取
        string type = context.Request.Form["type"];
        string tableName = context.Request.Form["table"];
        string Date = context.Request.Form["date"];
        string resulte = "";
        try
        {
            //建立连接对象
            SqlConnection conn = new SqlConnection();
            string dbName = "新冠肺炎疫情数据";
            string p_strUser = "sa";
            string p_strPWD = "a7758258";
            //string ConnectionString = String.Format("Data Source={0};Initial Catalog={1};User ID={2};PWD={3}", "(local)", dbName, p_strUser, p_strPWD);
            string ConnectionString = String.Format("Data Source={0};Initial Catalog={1};User ID={2};PWD={3}", 
                "DESKTOP-3D123F9", dbName, p_strUser, p_strPWD);
            conn.ConnectionString = ConnectionString;//连接数据库
            conn.Open();//打开数据库
            if (type == "select")
            {
                string sql = string.Format("SELECT * FROM {0} WHERE 时间=\'{1}\'", tableName,Date);//选择查询对应日期的数据
                SqlCommand cmd = new SqlCommand(sql, conn); //定义一个sql操作命令对象     
                SqlDataReader Reader = cmd.ExecuteReader(); //执行语句  
                                                            //遍历读取查询结果 
                while (Reader.Read())
                {
                    string name = Reader["省份"].ToString();
                    string date = Reader["时间"].ToString();
                    string confirm = Reader["确诊"].ToString();
                    string heal = Reader["治愈"].ToString();
                    string death = Reader["死亡"].ToString();
                    string new_confirm = Reader["新增确诊"].ToString();
                    resulte += string.Format("{{\"时间\":\"{0}\",\"省份\":\"{1}\"," +
                        "\"累积确诊\":\"{2}\",\"治愈\":\"{3}\",\"死亡\":" +
                        "\"{4}\",\"新增确诊\":\"{5}\"}}",
                        date, name, confirm,heal, death, new_confirm) + ","; //将查询结果拼接成json字符串
                }
                resulte = "[" + resulte.Remove(resulte.Length - 1, 1) + "]";
                cmd = null;
            }
           
            conn.Close(); //关闭连接            
            conn.Dispose(); //释放对象 
        }
        catch (Exception ex)
        {
            throw ex;//抛出异常
        }
        //返回结果到前台
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