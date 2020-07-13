public class cz {
    public static void main(String args[]) {
        Date date1=new Date();
        date1.setDate(2020,3,11);
        date1.print();
        date1.isLeapYear();
        int days1=date1.daysInMonth();
        System.out.println("该月共有"+days1+"天");
        boolean isleap1=date1.isLeapYear();
        Date datetomorrow1=date1.tomorrow();
        datetomorrow1.print();

        Date date2=new Date(2000,2,28);
        date2.print();
        int days2=date2.daysInMonth();
        System.out.println("该月共有"+days2+"天");
        boolean isleap2=date2.isLeapYear();
        Date datetomorrow2=date2.tomorrow();
        datetomorrow2.print();
    }
}
