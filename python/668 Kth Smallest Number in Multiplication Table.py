#credit to: https://www.youtube.com/watch?v=qvtYRm4reL4

class Solution:
    def findKthNumber(self, m: 'int', n: 'int', k: 'int') -> 'int':
        
        def lex(x, m, n, k):
            total = 0
            for i in range(1, min(m + 1, x + 1)):
                total += min(n, x // i)
                if total >= k:
                    return total
            return total

        l = 1
        r = m * n + 1
        while (l < r):
            x = l + (r - l) // 2
            if lex(x, m, n, k) >= k:
                r = x
            else:
                l = x + 1
        return l
