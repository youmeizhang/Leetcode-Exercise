class Solution(object):
    def minKBitFlips(self, A, K):
        ans = 0
        for i in range(len(A)):
            if A[i] == 0 and i + K <= len(A):
                ans += 1
                for j in range(K):
                    A[i + j] = 1 - A[i + j]
                    
        for i in range(len(A)):
            if A[i] == 0:
                return -1
        return ans
