import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class StudentList {
    public static int com_num(String filename) throws IOException {
        //读取学生个数
        BufferedReader bs = new BufferedReader(
                new FileReader(filename));
        int count=0;
        while((bs.readLine())!=null) count++;
        bs.close();
        return count-1;
    }
}
