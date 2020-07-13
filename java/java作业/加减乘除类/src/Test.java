public class Test {
    public static void main(String[] args){
        Add add=new Add();
        Subtract subtract=new Subtract();
        Multiplicate multiplicate=new Multiplicate();
        Devide devide=new Devide();
        int n=4, m=2;
        System.out.println("加法:");
        UseCompute.useCom(add,n,m);
        System.out.println("减法:");
        UseCompute.useCom(subtract,n,m);
        System.out.println("乘法:");
        UseCompute.useCom(multiplicate,n,m);
        System.out.println("除法:");
        UseCompute.useCom(devide,n,m);
    }
}
