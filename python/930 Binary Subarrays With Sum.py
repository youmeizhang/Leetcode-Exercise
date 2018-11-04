class Solution(object):
    def numSubarraysWithSum(self, A, S):
        d = collections.defaultdict(int)
        d[0] = 1
        tmp = 0
        res = 0
        n = len(A)
        for i in range(n):
            tmp += A[i]
            if tmp - S in d:
                res += d[tmp - S]
            d[tmp] += 1
        return res 
