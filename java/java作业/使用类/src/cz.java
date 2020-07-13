public class cz {
    public static void main(String[] args)
    {
        int selected;
        selected=(int)(1+Math.random()*3);
        selected=1;
        switch (selected){
            case 1:{
                Triangle triangle=new Triangle();
                triangle.getArea();
                triangle.getGirth();
            }break;
            case 2:{
                Rectangle rectangle=new Rectangle();
                rectangle.getArea();
                rectangle.getGirth();
            }break;
            case 3:{
                Circle circle=new Circle();
                circle.getArea();
                circle.getGirth();
            }break;
        }
    }
}

