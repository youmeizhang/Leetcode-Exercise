class Solution:
    def sortArrayByParity(self, A):
        if len(A) == 0: return []
        even, odd = [], []
        for i in A:
            if i % 2 == 0:
                even.append(i)
            elif i % 2 == 1:
                odd.append(i)
        return even + odd
