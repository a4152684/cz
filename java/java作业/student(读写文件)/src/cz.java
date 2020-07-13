import java.io.*;
import java.util.StringTokenizer;

public class cz {
    public static Student[] readData(String filename)
    {
        Student []students = new Student[0];
        try{
            BufferedReader bs = new BufferedReader(
                    new FileReader(filename));
            int count=0;
            while((bs.readLine())!=null) count++;
            bs.close();

            students = new Student[count-1];
            BufferedReader br = new BufferedReader(
                    new FileReader(filename));
            br.readLine();
            StringTokenizer st;
            String s;
            int i=0;
            while((s=br.readLine())!=null) {
                st = new StringTokenizer(s, ",");
                String id = st.nextToken();
                String name = st.nextToken();
                int[] score = new int[3];
                for (int j=0;j<score.length;j++) score[j]=Integer.parseInt(st.nextToken());
                students[i] = new Student(id, name, score);
                i++;
            }
        }
        catch(FileNotFoundException e)
        {
            System.out.println("File no found.");
        }
        catch(IOException e)
        {
            System.out.println("Read Error.");
        }
        catch(Exception e)
        {
            System.out.println(e.toString());
        }

        return students;
    }

    public static void writeData(Student[] students,String filename) throws Exception
    {
        PrintWriter pw = new PrintWriter(
                new BufferedWriter(
                        new FileWriter(filename)));
        int i;
        pw.println("学号,姓名,语文,数学,英语,总分");
        for(i=0;i<students.length;i++)
        {
            pw.println(students[i].Stu_Info());
            //pw.println(1);
        }
        pw.flush();
        pw.close();
    }
    public static void sort(Student []students)
    {
        int i, j;
        Student temp=new Student();
        int len=students.length;
        for (i=0; i<len-1; i++) //外循环为排序趟数，len个数进行len-1趟
            for (j=0; j<len-1-i; j++) { //内循环为每趟比较的次数，第i趟比较len-i次
                if (students[j].sum > students[j+1].sum) { //相邻元素比较，若逆序则交换（升序为左大于右，降序反之）
                    temp = students[j];
                    students[j] = students[j+1];
                    students[j+1] = temp;
                }
            }
    }
    public static void printStu(Student []students)
    {
        System.out.println("学号,姓名,语文,数学,英语,总分");
        for(int i=0;i<students.length;i++)
        {
            System.out.println(students[i].Stu_Info());
        }
    }
    public static void main(String args[])throws Exception{
        Student []stu;
        stu=readData("./test.txt");
        System.out.println("读取完毕，结果如下:");
        printStu(stu);
        sort(stu);
        System.out.println("排序完毕，结果如下:");
        printStu(stu);
        writeData(stu,"./result.txt");
        System.out.println("写入完毕");
    }
}
