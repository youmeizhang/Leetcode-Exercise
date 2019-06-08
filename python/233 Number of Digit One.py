# credit to: https://blog.csdn.net/xudli/article/details/46798619

class Solution(object):
    def countDigitOne(self, n):
        m = 1
        res = 0
        while m <= n:
            
            a = n // m
            b = n % m
            
            res += (a + 8) // 10 * m
            m *= 10
            if a % 10 == 1:
                res += (b + 1)
        return res
            
        """
        :type n: int
        :rtype: int
        """
        
