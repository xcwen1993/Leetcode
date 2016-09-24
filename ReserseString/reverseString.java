/**
 * Created by XiaochengWen on 16/9/24.
 */
public class reverseString {
    public String reverseString(String s) {
        char[] chars = s.toCharArray();
        int length = chars.length;
        int n = length - 1;
        char t;
        for (int i = n >> 1; i >= 0; i--) {
            int k = n - i;
            t = chars[i];
            chars[i] = chars[k];
            chars[k] = t;
        }
        return new String(chars);
    }
}
