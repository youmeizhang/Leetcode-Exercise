class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        n = len(S)
        l = [0] * (n+1)
        r = [0] * (n+1)
        
        for i in range(n):
            if S[i] == '0':
                l[i+1] = l[i]
            else:
                l[i+1] = l[i] + 1
        
        for i in range(n-1, -1, -1):
            if S[i] == '1':
                r[i] = r[i+1]
            else:
                r[i] = r[i+1] + 1
                
        res = float('inf')
        for i in range(-1, n):
            res = min(res, l[i+1] + r[i+1])
        return res
        
