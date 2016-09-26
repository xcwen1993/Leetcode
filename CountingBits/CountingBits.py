__author__ = 'XiaochengWen'
class Solution(object):
    def countBits(self, num):
        a=[0]
        while len(a)<=num:
            a+=[i+1 for i in a]
        return a[:num+1]
