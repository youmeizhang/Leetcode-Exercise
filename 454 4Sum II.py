class Solution:
    def fourSumCount(self, A, B, C, D):
        dic = collections.defaultdict(int)
        ans = 0
        for i in A:
            for j in B:
                dic[i + j] += 1
                
        for c in C:
            for d in D:
                ans += dic[-(c + d)]
                
        return ans    
