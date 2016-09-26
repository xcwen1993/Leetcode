__author__ = 'XiaochengWen'
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        r = ListNode(0)
        t = r
        while (l1 or l2):
            if not l1:
                x = l2.val+t.val
                l2 = l2.next
            else:
                if not l2:
                    x = l1.val+t.val
                    l1 = l1.next
                else:
                    x = l1.val+l2.val+t.val
                    l1 = l1.next
                    l2 = l2.next
            t.val = x%10
            if (l1 or l2 or (x//10)):
                t.next = ListNode(x//10)
                t = t.next
        return r