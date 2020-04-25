class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m == 0:
            return 0
        factor = 0
        while (m != n):
            m >>= 1
            n >>= 1
            factor += 1
        return m << factor
        
