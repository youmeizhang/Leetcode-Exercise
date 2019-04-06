#credit to: https://leetcode.com/problems/nth-digit/discuss/88417/4-liner-in-Python-and-complexity-analysis
class Solution(object):
    def findNthDigit(self, n):
        start, size, step = 1, 1, 9
        while n > size * step:
            n, start, size, step = n - size * step, start * 10, size + 1, step * 10
        #number that hold the digit
        num = start + (n - 1) // size
        
        #the pos
        return int(str(num)[(n - 1) % size])
        """
        :type n: int
        :rtype: int
        """
        
