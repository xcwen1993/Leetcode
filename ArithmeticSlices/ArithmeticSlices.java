/**
 * Created by XiaochengWen on 16/10/15.
 */
public class ArithmeticSlices {
    public int numberOfArithmeticSlices(int[] A) {
        int sum = 0;
        int i=0,j=0;
        int diff;
        while (i<A.length-2){
            j=i+1;
            diff = A[i+1]-A[i];
            while ((j+1<A.length) && (A[j+1]-A[j]==diff)) {
                j += 1;
            }
            sum += (j - i) * (j - i - 1)/2;
            i = j;
        }
        return sum;
    }
}
