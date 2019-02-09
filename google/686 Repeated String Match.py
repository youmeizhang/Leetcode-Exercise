class Solution:
    def repeatedStringMatch(self, A: 'str', B: 'str') -> 'int':
        lena = len(A)
        lenb = len(B)
        times = lenb // lena + 3
        for i in range(1, times):
            if B in A * i:
                return i
        return -1
    
