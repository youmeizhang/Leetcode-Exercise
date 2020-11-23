class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        def dfs(ring, idx):
            if idx == len(key):
                return 0
            
            if (ring, idx) in memo:
                return memo[(ring, idx)]

            n = len(ring)
            res = float('inf')
            for i in range(n):
                if ring[i] == key[idx]:
                    steps = min(i, n - i)
                    res = min(res, steps + 1 + dfs(ring[i:] + ring[0:i], idx + 1))
            memo[(ring, idx)] = res
            return res
        
        memo = {}
        return dfs(ring, 0)

        
