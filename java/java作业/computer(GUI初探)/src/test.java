import java.awt.*;
import java.awt.event.*;

public class test {
    Frame f=new Frame("Calculator");

    Label l1=new Label("Input Number1:");
    TextField t1=new TextField(15);
    Label l2=new Label("Input Number2:");
    TextField t2=new TextField(15);
    CheckboxGroup g=new CheckboxGroup();
    Checkbox box1=new Checkbox("+",false,g);
    Checkbox box2=new Checkbox("-",false,g);
    Checkbox box3=new Checkbox("*",false,g);
    Checkbox box4=new Checkbox("/",false,g);
    Button b1=new Button("Calculate");
    Button b2=new Button("Clear");
    Label l3=new Label("Result:");
    Label l4=new Label("");

    Panel p1=new Panel();   Panel p2=new Panel();   Panel p3=new Panel();   Panel p4=new Panel();
    Panel p5=new Panel();   Panel p6=new Panel();   Panel p7=new Panel();   Panel p8=new Panel();

    public static void main(String[] args){
        test t0=new test();
        t0.Set();
    }

    void Set(){
        f.setLayout(new GridLayout(0,2));

        b1.addActionListener(new Handle());
        b2.addActionListener(new Handle());

        p1.add(l1);     p2.add(t1);
        p3.add(l2);     p4.add(t2);
        p5.add(box1);   p5.add(box2);
        p6.add(box3);   p6.add(box4);
        p7.add(b1);     p8.add(b2);

        l3.setAlignment(1);
        l4.setAlignment(0);
        f.add(p1);  f.add(p2);  f.add(p3);  f.add(p4);  f.add(p5);
        f.add(p6);  f.add(p7);  f.add(p8);  f.add(l3);  f.add(l4);

        f.setSize(400,300);
        f.setLocation(300,100);

        f.addWindowListener(new WindowAdapter() {
            @Override
            public void windowClosing(WindowEvent e) {
                System.exit(0);
            }
        });

        f.setVisible(true);
    }

    class Handle implements ActionListener {
        public void actionPerformed(ActionEvent e) {
            if(e.getSource()==b1){
                double number1=Double.parseDouble(t1.getText());
                double number2=Double.parseDouble(t2.getText());
                double result=0;
                //获得单选框选中的运算符
                Checkbox operator=g.getSelectedCheckbox();
                switch (operator.getLabel()){
                    case "+":result=number1+number2;break;
                    case "-":result=number1-number2;break;
                    case "*":result=number1*number2;break;
                    case "/":result=number1/number2;break;
                }
                l4.setText(String.format("%.2f",result));
            }

            else if(e.getSource()==b2){
                t1.setText("");
                t2.setText("");
                l4.setText("");
            }
        }
    }
}
