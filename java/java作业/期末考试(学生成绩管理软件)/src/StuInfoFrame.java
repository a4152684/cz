import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;

public class StuInfoFrame {
    public Student []stu=new Student[0];

    Frame f=new Frame("学生信息管理");

    Button b1=new Button("import");
    Button b2=new Button("sort");
    Button b3=new Button("exit");
    Button b4=new Button("search");
    TextArea t1=new TextArea(10,95);
    TextField t2=new TextField(30);
    Label l=new Label("id：");
    CheckboxGroup g=new CheckboxGroup();
    Checkbox box1=new Checkbox("Ascending",false,g);
    Checkbox box2=new Checkbox("Descending",false,g);
    Panel p1=new Panel();
    Panel pp1=new Panel();
    Panel p2=new Panel();
    Panel p3=new Panel();

    void set()
    {
        f.setLayout(new GridLayout(0,1));

        b1.addActionListener(new Handle());
        b2.addActionListener(new Handle());
        b3.addActionListener(new Handle());
        b4.addActionListener(new Handle());

        box1.setState(true);
        //b1.setSize(30,30);

        //p1.setSize(10,10);
        p1.setLayout(new GridLayout(1,3));
        pp1.setLayout(new GridLayout(1,3));
        pp1.add(box1); pp1.add(box2); pp1.add(b2);
        p1.add(b1);  p1.add(pp1); p1.add(b3);
        p2.add(t1);
        p3.add(l); p3.add(t2); p3.add(b4);

        f.add(p1);
        f.add(p2);
        f.add(p3);

        f.setSize(800,500);
        f.setLocation(300,100);
        f.setVisible(true);

        f.addWindowListener(new WindowAdapter() {
            @Override
            public void windowClosing(WindowEvent e) {
                System.exit(0);
            }
        });
    }

    class Handle implements ActionListener {

        public void actionPerformed(ActionEvent e) {
            if (e.getSource() == b1) {

                try {
                    stu = Student.readData("./student.txt");
                }
                catch (Exception e1) {}
                //下面将stu的信息放入textfield
                //t1.setText("");
                String str = "";
                t1.setText("学号\t姓名\t成绩1\t成绩2\t成绩3\t总分\n");
                for (int i = 0; i < stu.length; i++) {
                    //if(stu[i]!=null)
                    str += stu[i].Stu_Info() + "\n";
                    //else JOptionPane.showMessageDialog(null, "null", "数组为空", JOptionPane.ERROR_MESSAGE);
                }
                t1.append(str);
                //System.out.println("22");
            }

            else if(e.getSource()==b2){
                Student.sort(stu);
                //下面将stu的信息重新放入textfield
                Checkbox operator=g.getSelectedCheckbox();
                if(stu.length==0){
                    JOptionPane.showMessageDialog(null, "请导入数据", "数组为空", JOptionPane.ERROR_MESSAGE);
                }
                else if(operator.getLabel()=="Ascending"){
                    String str="";
                    //System.out.println("Asc");
                    for(int i=0;i<stu.length;i++){
                        if(stu[i]!=null)
                            str+=stu[i].Stu_Info()+"\n";
                        else JOptionPane.showMessageDialog(null, "null", "数组为空", JOptionPane.ERROR_MESSAGE);
                    }
                    t1.setText("学号\t姓名\t成绩1\t成绩2\t成绩3\t总分\n");
                    t1.append(str);
                }
                else {
                    //System.out.println("Des");
                    String str="";
                    for(int i=stu.length-1;i>=0;i--){
                        if(stu[i]!=null)
                            str+=stu[i].Stu_Info()+"\n";
                        else JOptionPane.showMessageDialog(null, "null", "数组为空", JOptionPane.ERROR_MESSAGE);
                    }
                    t1.setText("学号\t姓名\t成绩1\t成绩2\t成绩3\t总分\n");
                    t1.append(str);
                }
            }

            else if(e.getSource()==b3){
                System.exit(0);//退出
            }

            else if(e.getSource()==b4){
                //查找
                if(stu.length==0){
                    JOptionPane.showMessageDialog(null, "请导入数据", "数组为空", JOptionPane.ERROR_MESSAGE);
                }
                else{
                    String id=t2.getText();
                    //System.out.println(id);
                    int i;
                    for(i=0;i<stu.length;i++){//System.out.println(stu[i].id);
                        if(stu[i].id.equals(id)){
                            t1.setText("学号\t姓名\t成绩1\t成绩2\t成绩3\t总分\n");
                            t1.append(stu[i].Stu_Info());
                            break;
                        }
                    }
                    if(i==stu.length) {
                        JOptionPane.showMessageDialog(null, "查找失败", "没有此学号", JOptionPane.ERROR_MESSAGE);
                    }
                }
                }
            }
        }
    }

