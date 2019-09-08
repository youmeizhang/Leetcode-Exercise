class Solution:
    def longestMountain(self, A: List[int]) -> int:
        n = len(A)
        res = 0
        for i in range(1, n-1):
            if A[i] > A[i-1] and A[i] > A[i+1]:
                l = i - 1
                r = i + 1
                tmp = 3

                while (l > 0 and A[l] > A[l-1]):
                    tmp += 1
                    l -= 1
                
                while r < n - 1 and A[r] > A[r+1]:
                    tmp += 1
                    r += 1

                res = max(res, tmp)
        return res
