abstract class Shape
{
    double Area, Girth;
    void  getArea();
    void  getGirth();
}

class Triangle extends  Shape
{
    double L1, L2, L3;
    Triangle()
    {
        boolean isTriangle=0;
        while (!isTriangle) {
            L1 = 1 + Math.random() * 10;
            L2 = 1 + Math.random() * 10;
            L3 = 1 + Math.random() * 10;
            if (L1+L2>L3 && L1+L3>L2 && L2+L3>L1)
            {
                isTriangle=1;
            }
        }
        this.L1=L1;
        this.L2=L2;
        this.L3=L3;
        System.out.println("该三角形三边长为"+L1+L2+L3);
    }

    @java.lang.Override
    void getArea() {
        double P=(L1+L2+L3)/2;
        Area=Math.sqrt(P*(P-L1)*(P-L2)*(P-L3));
        System.out.println("该三角形面积为"+Area);
    }

    @java.lang.Override
    void getGirth() {
        Girth=L1+L2+L3;
        System.out.println("该三角形周长为"+Girth);
    }
}

class Rectangle extends Shape
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

class Circle extends Shape
{
    double r;
    const double PI= 3.1415926;
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