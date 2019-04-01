class Solution(object):
    def prefixesDivBy5(self, A):
        n = len(A)
        res = [False] * n
        s = ''
        for i in range(n):
            s += str(A[i])
            if int(s, 2) % 5 == 0:
                res[i] = True
        return res
        """
        :type A: List[int]
        :rtype: List[bool]
        """
        
