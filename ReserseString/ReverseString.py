__author__ = 'XiaochengWen'
class Solution(object):
    def reverseString(self, s):
        a = list(s)
        i=0
        while 2*i<len(s)-1:
            a[i],a[len(s)-i-1] = a[len(s)-i-1],a[i]
            i+=1
        return ''.join(a)
a = Solution()
print(a.reverseString("djasf"))
