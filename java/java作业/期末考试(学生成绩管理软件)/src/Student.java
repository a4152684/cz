import javax.swing.*;
import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Student {
    String id;
    String name;
    int []score;
    int sum;
    Student()
    {
        id="";
        name="";
        sum=0;
        score=new int[0];
    }
    Student(String id,String name,int []score) throws ScoreException {
        sum=0;
        this.id=id;
        this.name=name;
        this.score=score;
        for(int i=0;i<score.length;i++)
        {
            sum+=score[i];
            if (score[i] < 0 || score[i] > 100)
                throw new ScoreException();
        }
    }

    public String Stu_Info()
    {
        String s="";
        s=id+"\t"+name+"\t";
        for(int i=0;i<score.length;i++)
        {
            s+=score[i]+"\t";
        }
        s+=sum;
        return s;
    }

    public static Student[] readData(String filename) throws ScoreException
    {
        Student []students = new Student[0];
        try{
            //读取学生个数
            int count=StudentList.com_num(filename);

            students = new Student[count];
            BufferedReader br = new BufferedReader(
                    new FileReader(filename));
            br.readLine();
            StringTokenizer st;
            String s;
            int i=0;
            while((s=br.readLine())!=null) {
                st = new StringTokenizer(s, "\t");
                String id = st.nextToken();
                String name = st.nextToken();
                int[] score = new int[3];
                for (int j=0;j<score.length;j++) {
                    int grade=Integer.parseInt(st.nextToken());
                    score[j] = grade ;
                }
                try {
                    students[i] = new Student(id, name, score);
                }
                catch (ScoreException e1) {
                    JOptionPane.showMessageDialog(null, e1.get_err(),"导入失败",  JOptionPane.ERROR_MESSAGE);
                }
                //System.out.println(i);
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

}
