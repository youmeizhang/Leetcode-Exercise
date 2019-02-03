class Solution:
    def sumEvenAfterQueries(self, A: 'List[int]', queries: 'List[List[int]]') -> 'List[int]':
        total = 0
        res = []
        
        for i in range(len(A)):
            if A[i] % 2 == 0:
                total += A[i]
                
        for query in queries:
            if A[query[1]] % 2 == 0:
                total -= A[query[1]]
            A[query[1]] += query[0]
            if A[query[1]] % 2 == 0:
                total += A[query[1]]
            res.append(total)
        return res
