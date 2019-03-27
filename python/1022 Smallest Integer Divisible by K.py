#credit to: https://blog.csdn.net/fuxuemingzhu/article/details/88778532

class Solution(object):
    def smallestRepunitDivByK(self, K):
        if K % 2 not in (1, 3, 7, 9):
            return -1
        r = 0
        for i in range(1, K+1):
            r = (10 * r + 1) % K

            if r == 0:
                return i
        return -1
        
        """
        :type K: int
        :rtype: int
        """
        
