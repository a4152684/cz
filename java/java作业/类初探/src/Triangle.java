public class Triangle extends  Shape
{
    double L1, L2, L3;
    Triangle()
    {
        boolean isTriangle=false;
        while (!isTriangle) {
            L1 = 1 + Math.random() * 10;
            L2 = 1 + Math.random() * 10;
            L3 = 1 + Math.random() * 10;
            if (L1+L2>L3 && L1+L3>L2 && L2+L3>L1)
            {
                isTriangle=true;
            }
        }
        this.L1=L1;
        this.L2=L2;
        this.L3=L3;
        System.out.println("该三角形三边长为"+L1+","+L2+","+L3);
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
