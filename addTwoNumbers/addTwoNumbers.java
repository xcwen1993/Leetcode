/**
 * Created by XiaochengWen on 16/9/24.
 */


class ListNode {
      int val;
      ListNode next;
      ListNode(int x) { val = x; }
  }

public class addTwoNumbers {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode ret = new ListNode(0);
        ListNode curr = ret;
        ListNode a = l1,b=l2;
        while (a!=null || b!=null){
            int x = (a != null) ? a.val : 0;
            int y = (b != null) ? b.val : 0;
            int sum = x+y+curr.val;
            if (a != null) a = a.next;
            if (b != null) b = b.next;
            curr.val = sum%10;
            if ((a!=null) || (b!=null) || (sum/10!=0)) {
                curr.next = new ListNode(sum / 10);
                curr = curr.next;
            }
        }
        return ret;
    }
}
