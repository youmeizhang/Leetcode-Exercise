class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        n = len(A)
        res = float('-inf')
        for i in range(n):
            for j in range(i+1, n):
                if A[i] + A[j] < K:
                    res = max(res, A[i]+A[j])
        return res if res != float('-inf') else -1
        
