#TL
class Solution:
    def threeEqualParts(self, A):
        n = len(A)
        for i in range(n):
            for j in range(i+1, n-1):
                first = A[0:i+1]
                second = A[i+1:j+1]
                third = A[j+1:]
                
                f = int(''.join(str(x) for x in first), 2)
                s = int(''.join(str(x) for x in second), 2)
                t = int(''.join(str(x) for x in third), 2)
                
                if f == s and s == t:
                    return [i, j+1]
        return [-1, -1]
