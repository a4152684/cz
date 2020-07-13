import java.util.Scanner;

public class cz {
    public static void main(String args[]) throws DateException{
        Scanner s = new Scanner(System.in);
        int year,month,day;
        Date date = new Date();

        boolean flag=true;
        while (flag) {
            try {
                System.out.println("请输入年，月，日，以空格隔开");
                year=s.nextInt();
                month=s.nextInt();
                day=s.nextInt();
                date.setDate(year,month,day);
                date.print();
            } catch (DateException e) {
                System.out.println(e.get_type());
            }
            finally {
                System.out.println("输入1可重新设置日期，其他退出");
                if(s.nextInt()==1)
                {
                    flag=true;
                }
                else{
                    flag=false;
                }
            }
        }
    }
}

