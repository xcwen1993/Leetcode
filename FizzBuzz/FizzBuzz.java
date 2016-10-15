import java.util.ArrayList;
import java.util.List;

/**
 * Created by XiaochengWen on 16/10/15.
 */
public class FizzBuzz {
    public List<String> fizzBuzz(int n) {
        ArrayList<String> out = new ArrayList<String>();
        for (Integer i=1;i<=n;i++){
            String a = "";
            if (i%3==0){
                a += "Fizz";
            }
            if (i%5==0){
                a += "Buzz";
            }
            if (a==""){
                a = i.toString();
            }
            out.add(a);
        }
        return out;
    }
}
