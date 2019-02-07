class Solution:
    def constructArray(self, n: 'int', k: 'int') -> 'List[int]':
        res = [i for i in range(1, n+1)]
        j = 1
        while j < k:
            res = res[:j] + list(reversed(res[j:]))
            j += 1
        return res
