__author__ = 'XiaochengWen'
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        out = []
        for i in range(1,n+1):
            a = ""
            if (i%3==0):
                a += "Fizz"
            if (i%5==0):
                a += "Buzz"
            if (not a):
                a = str(i)
            out.append(a)
        return out