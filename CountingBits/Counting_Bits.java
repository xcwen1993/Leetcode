/**
 * Created by XiaochengWen on 16/9/24.
 */
public class Counting_Bits {
    public int[] countBits(int num) {
        int[] answer = new int[num + 1];
        answer[0] = 0;
        for (int i = 1; i <= num; i++) {
            answer[i] = i % 2 + answer[i / 2];
        }
        return answer;
    }
}
