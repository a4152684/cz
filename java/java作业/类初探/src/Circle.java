
public class Circle extends Shape
{
    double r;
    double PI= 3.1415926;
    Circle(){
        r= 1 + Math.random() * 10;
        System.out.println("该圆形半径为"+r);
    }

    @java.lang.Override
    void getArea() {
        Area=PI*r*r;
        System.out.println("该圆形面积为"+Area);
    }

    @java.lang.Override
    void getGirth() {
        Girth=2*PI*r;
        System.out.println("该圆形周长为"+Girth);
    }
}
