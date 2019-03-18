class Solution(object):
    def fib(self, N):
        dic = {}
        
        def helper(N):
            if N in dic:
                return dic[N]
            elif N < 2:
                return N
            else:
                res = helper(N-1) + helper(N-2)
            dic[N] = res
            return res
        
        return helper(N)
        """
        :type N: int
        :rtype: int
        """
        
