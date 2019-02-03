class Solution:
    def intervalIntersection(self, A: 'List[Interval]', B: 'List[Interval]') -> 'List[Interval]':
        i = 0
        j = 0
        
        lena = len(A)
        lenb = len(B)
        res = []
        
        while (i < lena - 1 and j < lenb - 1):
            a = max(A[i].start, B[j].start)
            b = min(A[i].end, B[j].end)
            if a <= b:
                res.append([a, b])
            if B[j].end >= A[i+1].start:
                i += 1
            elif A[i].end >= B[j+1].start:
                j += 1
            else:
                i += 1
                j += 1
        if i == lena - 1:        
            while(j != lenb):
                a = max(A[i].start, B[j].start)
                b = min(A[i].end, B[j].end)
                if a <= b:
                    res.append([a, b])
                j += 1
        elif j == lenb - 1:
            while(i != lena):
                a = max(A[i].start, B[j].start)
                b = min(A[i].end, B[j].end)
                if a <= b:
                    res.append([a, b])
                i += 1
     
        return res
