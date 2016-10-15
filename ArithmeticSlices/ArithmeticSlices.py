__author__ = 'XiaochengWen'

class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        sum = 0
        i=0
        while (i<len(A)-2):
            diff = A[i+1]-A[i]
            j=i+1
            while (j+1<len(A)) and (A[j+1]-A[j]==diff):
                j += 1
            sum += (j-i)*(j-i-1)//2
            i=j
        return sum

aa = Solution()
print(aa.numberOfArithmeticSlices([1, 2, 3, 4]))