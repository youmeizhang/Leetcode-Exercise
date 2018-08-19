#time limit
class Solution:
    def fairCandySwap(self, A, B):

        a = sum(A)
        b = sum(B)
        
        B= list(sorted(set(B)))
        n = len(B)
        
        A = list(sorted(set(A)))
        
        m = len(A)
        
        ans = [0, 0]
        each = (a - b) / 2
        for i in range(m):
            try:
                idx = B.index(-each + A[i])
            except ValueError:
                idx = -1
            if idx == -1:
                continue
            else:
                ans = [A[i], B[idx]]
                break
        return ans
