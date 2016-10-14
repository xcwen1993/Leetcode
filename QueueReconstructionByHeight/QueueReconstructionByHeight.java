import java.util.*;

/**
 * Created by XiaochengWen on 16/10/14.
 */
public class QueueReconstructionByHeight {
    public int[][] reconstructQueue(int[][] people) {
        Arrays.sort(people, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                if (o1[0]!=o2[0]){
                    return o2[0]-o1[0];
                }else {
                    return o1[1]-o2[1];
                }
            }
        });
        ArrayList<int[]> out = new ArrayList<int[]>();
        for (int[] i : people){
            out.add(i[1],i);
        }
        return out.toArray(new int[people.length][]);
    }
}
