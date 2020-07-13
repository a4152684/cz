using System;
using System.IO;

namespace file_deal2
{
    class Program
    {
        static int n1 = 1, n2 = 1, n3 = 1, n4 = 1;
        public static void create(string filename)
        {
            if (!Directory.Exists(filename))
            {
                Directory.CreateDirectory(filename);//无则创建文件夹
                Console.WriteLine("结果文件夹创建成功\n");
            }
        }
      

        public static void dir_de(FileSystemInfo folder2)
        {
            DirectoryInfo folder = new DirectoryInfo(folder2.FullName);
            foreach (FileSystemInfo fileSystem in folder.GetFileSystemInfos(""))//对目录下的每个文件或目录
            {
                if (fileSystem is DirectoryInfo)//如果是目录，则复制
                {
                    string filename = fileSystem.FullName;
                    string[] filename_split = filename.Split("\\");
                    int length = filename_split.Length;
                    string str = filename_split[length - 1];                  
                    string[] str_split = str.Split("_");
                    if(str_split.Length<3) break;
                    string s1 = str_split[str_split.Length - 3];
                    string s2 = str_split[str_split.Length - 2];
                    if(string.Equals(s1, "RIGHT") && string.Equals(s2, "CC"))
                    {
                        string s = "./结果/";
                        s += "1-" + n1.ToString();
                        n1++;
                        Directory.Move(filename, s);
                    }
                    else if (string.Equals(s1,"RIGHT")&&string.Equals(s2,"MLO"))
                    {
                        string s = "./结果/";
                        s += "2-" + n2.ToString();
                        n2++;
                        Directory.Move(filename, s);
                    }
                    else if (string.Equals(s1, "LEFT") && string.Equals(s2, "CC"))
                    {
                        string s = "./结果/";
                        s += "3-" + n3.ToString();
                        n3++;
                        Directory.Move(filename, s);
                    }
                    else if(string.Equals(s1, "LEFT") && string.Equals(s2, "MLO"))
                    {
                        string s = "./结果/";
                        s += "4-" + n4.ToString();
                        n4++;
                        Directory.Move(filename, s);
                    }


                }
                else //如果是文件,跳过
                {
                    
                }
            }
        }

        static void Main(string[] args)
        {
            create("./结果");
            Console.WriteLine("Hello World!");
            DirectoryInfo folder = new DirectoryInfo("./");
            dir_de(folder);

            Console.WriteLine("\n再见");
            Console.ReadKey();

        }
    }
}
