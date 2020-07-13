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
    Student(String id,String name,int []score)
    {
        sum=0;
        this.id=id;
        this.name=name;
        this.score=score;
        for(int i=0;i<score.length;i++)
        {
            sum+=score[i];
        }
    }
    public String Stu_Info()
    {
        String s="";
        s=id+","+name+",";
        for(int i=0;i<score.length;i++)
        {
            s+=score[i]+",";
        }
        s+=sum;
        return s;
    }
}
