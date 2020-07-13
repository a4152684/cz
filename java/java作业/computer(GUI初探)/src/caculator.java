import java.awt.*;
import java.awt.event.*;

class caculator
{
    Frame f=new Frame("A Caculator");

    Label l1=new Label("input the first number:");
    Label l2=new Label("input the second number:");
    Label l3=new Label("result:");
    Label l4=new Label();
    Button b1=new Button("caculate");
    Button b2=new Button("delete");
    TextField t1=new TextField(15);
    TextField t2=new TextField(15);
    CheckboxGroup g=new CheckboxGroup();
    Checkbox box1=new Checkbox("+",false,g);
    Checkbox box2=new Checkbox("-",false,g);
    Checkbox box3=new Checkbox("*",false,g);
    Checkbox box4=new Checkbox("/",false,g);

    Panel p1=new Panel();
    Panel p2=new Panel();
    Panel p3=new Panel();
    Panel p4=new Panel();
    Panel p5=new Panel();
    Panel p6=new Panel();
    Panel p7=new Panel();
    Panel p8=new Panel();
    Panel p9=new Panel();
    Panel p10=new Panel();

    public void set()
    {
        f.setLayout(new GridLayout(0,2));

        p1.add(l1);
        p2.add(t1);
        p3.add(l2);
        p4.add(t2);
        p5.add(box1);
        p5.add(box2);
        p6.add(box3);
        p6.add(box4);
        p7.add(b1);
        p8.add(b2);
        p9.add(l3);
        p10.add(l4);

        f.add(p1);f.add(p2);
        f.add(p3);f.add(p4);
        f.add(p5);f.add(p6);
        f.add(p7);f.add(p8);
        //f.add(p9);f.add(p10);
        f.add(p9); f.add(l4);

        f.setVisible(true);
        f.setLocation(200,200);
        f.setSize(400,350);

        b1.addActionListener(new Handle());
        b2.addActionListener(new Handle());

        f.addWindowListener(new Win());
    }
    class Handle implements ActionListener {
        @Override
        public void actionPerformed(ActionEvent e) {
            if(e.getSource()==b1)
            {
                double n1=Double.parseDouble(t1.getText());
                double n2=Double.parseDouble(t2.getText());
                double ans=0;
                switch (g.getSelectedCheckbox().getLabel())
                {
                    case "+": ans=n1+n2; break;
                    case "-": ans=n1-n2; break;
                    case "*": ans=n1*n2; break;
                    case "/":
                        if(n2==0) {
                            System.out.println("the second number can't equal 0");
                            break;
                        }
                        else{
                            ans=n1/n2;
                        }
                }
                l4.setText(String.valueOf(ans));
            }
            else if(e.getSource()==b2)
            {
                t1.setText("");
                t2.setText("");
                l4.setText("");
            }
        }
    }
    class Win implements WindowListener{

        @Override
        public void windowOpened(WindowEvent windowEvent) {

        }

        @Override
        public void windowClosing(WindowEvent windowEvent) {
            System.exit(0);
        }

        @Override
        public void windowClosed(WindowEvent windowEvent) {

        }

        @Override
        public void windowIconified(WindowEvent windowEvent) {

        }

        @Override
        public void windowDeiconified(WindowEvent windowEvent) {

        }

        @Override
        public void windowActivated(WindowEvent windowEvent) {

        }

        @Override
        public void windowDeactivated(WindowEvent windowEvent) {

        }
    }
    public static void main(String[] args) {
        caculator Cac=new caculator();
        Cac.set();
    }
}