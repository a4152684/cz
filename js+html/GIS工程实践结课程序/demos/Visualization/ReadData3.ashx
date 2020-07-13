<%@ WebHandler Language="C#" Class="ReadData" %>

using System;
using System.Web;
using System.Text;
using System.Data;
using System.Data.SqlClient;
using System.Collections;
public class ReadData : IHttpHandler
{
    public string[] sort(int[] list,string [] name)
    {
        int temp;
        string tempS;
        for (int i = 0; i < list.Length - 1; i++)
        {
            for (int j = 1; j < list.Length - i - 1; j++)
            {
                if (list[j - 1] < list[j])
                {
                    temp = list[j - 1];
                    list[j - 1] = list[j];
                    list[j] = temp;

                    tempS = name[j - 1];
                    name[j - 1] = name[j];
                    name[j] = tempS;
                }
            }
        }
        return name;
    }
    public void ProcessRequest(HttpContext context)
    {
        //POST请求的参数获取
        string type = context.Request.Form["type"];
        string tableName = "疫情数据";
        string Date = context.Request.Form["date"];
        string DataType=context.Request.Form["dataType"];
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
            conn.ConnectionString = ConnectionString;//连接数据库
            conn.Open();//打开数据库
            if (type == "select")
            {
                string sql = string.Format("SELECT * FROM {0} WHERE 时间=\'{1}\'", tableName,Date);;
                SqlCommand cmd1 = new SqlCommand(sql, conn); //定义一个sql操作命令对象     
                SqlDataReader Reader1 = cmd1.ExecuteReader(); //执行语句  
                int []list =new int[34];
                string[] nameS = new string[34];
                int i = 0;

                while (Reader1.Read())
                {
                    nameS[i] = Reader1["省份"].ToString();
                    if (DataType == "累积确诊")
                    {
                        list[i] = Convert.ToInt32(Reader1["确诊"].ToString());
                    }
                    else if (DataType == "治愈")
                    {
                        list[i] = Convert.ToInt32(Reader1["治愈"].ToString());
                    }
                    else if (DataType == "死亡")
                    {
                        list[i] = Convert.ToInt32(Reader1["死亡"].ToString());
                    }
                    else
                    {
                        list[i] = Convert.ToInt32(Reader1["新增确诊"].ToString());
                    }
                    i++;
                }
                conn.Close(); //关闭连接            
                conn.Dispose(); //释放对象 

                conn.ConnectionString = ConnectionString;//连接数据库
                conn.Open();//打开数据库
                nameS = sort(list, nameS);//排序
                //选择查询
                sql=string.Format("SELECT * FROM {0} WHERE 时间=\'{1}\' AND " +
                    "(省份= \'{2}\' OR 省份= \'{3}\' OR 省份= \'{4}\')",
                    tableName,Date,nameS[0],nameS[1],nameS[2]);
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
                resulte = "[" + resulte.Remove(resulte.Length - 1, 1) + "]";
                cmd = null;
            }
            else if (type == "insert")
            {
                string geo = context.Request.Form["geo"];
                string att = context.Request.Form["att"];
                string sql = string.Format("INSERT into 疫情数据2 values('{0}','{1}',{2},{3},{4},{5},'{6}')",
                    att.Split(',')[0], att.Split(',')[1],
                    Convert.ToDecimal(att.Split(',')[2]), Convert.ToDecimal(att.Split(',')[3]),
                    Convert.ToDecimal(att.Split(',')[4]), Convert.ToDecimal(att.Split(',')[5]),geo);//插入查询
                SqlCommand cmd = new SqlCommand(sql, conn); //定义一个sql操作命令对象 
                if (cmd.ExecuteNonQuery() == 1)
                {
                    resulte = "添加成功！";
                }
            }
            else if (type == "delete")
            {
                string Name = context.Request.Form["name"];
                string sql = string.Format("DELETE FROM 疫情数据2 WHERE 名字='{0}'",Name);//删除查询
                SqlCommand cmd = new SqlCommand(sql, conn); //定义一个sql操作命令对象 
                if (cmd.ExecuteNonQuery() == 1)
                {
                    resulte = "删除成功！";
                }

            }
            else if (type=="select2")
            {
                string sql = string.Format("SELECT * FROM 疫情数据2");//选择查询对应日期的数据
                SqlCommand cmd = new SqlCommand(sql, conn); //定义一个sql操作命令对象     
                SqlDataReader Reader = cmd.ExecuteReader(); //执行语句  
                                                            //遍历读取查询结果 
                while (Reader.Read())
                {
                    string name = Reader["名字"].ToString();
                    string date = Reader["时间"].ToString();
                    string confirm = Reader["确诊"].ToString();
                    string heal = Reader["治愈"].ToString();
                    string death = Reader["死亡"].ToString();
                    string new_confirm = Reader["新增确诊"].ToString();
                    string Geometry = Reader["Geometry"].ToString();
                    resulte += string.Format("{{\"时间\":\"{0}\",\"省份\":\"{1}\"," +
                        "\"累积确诊\":\"{2}\",\"治愈\":\"{3}\",\"死亡\":" +
                        "\"{4}\",\"新增确诊\":\"{5}\",\"Geometry\":\"{6}\"}}",
                        date, name, confirm,heal, death, new_confirm,Geometry) + ","; //将查询结果拼接成json字符串
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