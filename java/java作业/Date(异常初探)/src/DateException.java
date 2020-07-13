public class DateException extends Exception {
    String err_type;
    DateException(int i)
    {
        switch (i){
            case 1:err_type="年份错误！"; break;
            case 2:err_type="月份错误！"; break;
            case 3:err_type="日期错误！"; break;
        }
    }
    public String get_type()
    {
        return err_type;
    }
}
