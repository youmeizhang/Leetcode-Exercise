class Solution:
    def countVowelStrings(self, n: int) -> int:
        visited = {}
        def dp(n, k):
            if k == 1: return 1
            if n == 1: return k
            if (n, k) in visited:
                return visited[n, k]
            total = 0
            for i in range(1, k+1):
                total += dp(n-1, i)
            visited[n, k] = total
            return visited[n, k]
    
        return dp(n, 5)
            
