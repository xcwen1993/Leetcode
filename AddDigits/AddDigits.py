class Solution(object):
    def addDigits(self, num):
        return num and (num%9 or 9) or 0

    def addDigits_1(self, num):
        return (num%9 or 9) if num else 0