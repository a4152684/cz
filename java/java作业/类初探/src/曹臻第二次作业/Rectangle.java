public class Rectangle extends Shape
{
    double a,b;
    Rectangle(){
        a = 1 + Math.random() * 10;
        b = 1 + Math.random() * 10;
        if(b>a)
        {
            System.out.println("该矩形长为"+b+"，宽为"+a);
        }
        else {
            System.out.println("该矩形长为"+a+"，宽为"+b);
        }
    }

    @java.lang.Override
    void getArea() {
        Area=a*b;
        System.out.println("该矩形面积为"+Area);
    }

    @java.lang.Override
    void getGirth() {
        Girth=2*(a+b);
        System.out.println("该矩形周长为"+Girth);
    }
}