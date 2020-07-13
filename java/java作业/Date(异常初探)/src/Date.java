public class Date  {
    int year;
    int month;
    int day;

    Date()
    {

    }
    Date(int year, int month, int day) throws DateException {
        if(year>=0){
            this.year=year;
        }
        else{
            this.year=0;
            //System.out.println("年份应为非负数");
            throw new DateException(1);
        }
        if(month>=1&&month<=12){
            this.month=month;
        }
        else{
            this.month=0;
            //System.out.println("月份应为1-12间的整数");
            throw new DateException(2);
        }
        if(day>=1&&day<=daysInMonth()){
            this.day=day;
        }
        else{
            this.day=0;
            //System.out.println("日期不应超过该月最大和最小范围");
            throw new DateException(3);
        }
    }

    void setDate(int year,int month,int day) throws DateException{
        if(year>=0){
            this.year=year;
        }
        else{
            this.year=0;
            //System.out.println("年份应为非负数");
            throw new DateException(1);
        }
        if(month>=1&&month<=12){
            this.month=month;
        }
        else{
            this.month=0;
            //System.out.println("月份应为1-12间的整数");
            throw new DateException(2);
        }
        if(day>=1&&day<=daysInMonth()){
            this.day=day;
        }
        else{
            this.day=0;
            //System.out.println("日期不应超过该月最大和最小范围");
            throw new DateException(3);
        }
    }

    void print()
    {
        System.out.println("日期为："+year+"年"+month+"月"+day+"日");
    }

    boolean isLeapYear()
    {
        if(year%4!=0||(year%100==0&&year%400!=0))
        {
            return false;
        }
        else
        {
            return true;
        }
    }

    int daysInMonth()
    {
        switch (month){
            case 1:
            case 3:
            case 5:
            case 7:
            case 8:
            case 10:
            case 12:
                return 31;
            case 4:
            case 6:
            case 9:
            case 11:
                return 30;
            case 2:
                if(isLeapYear())
                    return 29;
                else
                    return 28;
            default:
                return 0;
        }
    }

    Date tomorrow() throws  DateException{
        Date DateTomorrow=new Date(year,month,day);
        if(day==daysInMonth()){
            if(month!=12){
                DateTomorrow.setDate(year,month+1,1);
            }
            else{
                DateTomorrow.setDate(year+1,1,1);
            }
        }
        else{
            DateTomorrow.setDate(year,month,day+1);
        }

        return DateTomorrow;
    }
}
