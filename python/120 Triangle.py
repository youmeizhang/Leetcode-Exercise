class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        row = len(triangle)
        col = len(triangle[-1])
        dp = [[0] * col for _ in range(row)]
        dp[0] = triangle[0]
        
        for i in range(1, row):
            n = len(triangle[i])
            for j in range(n):
                p = max(0, j-1)
                q = min(len(triangle[i-1])-1, j)
                dp[i][j] = min(dp[i-1][p], dp[i-1][q]) + triangle[i][j]
        return min(dp[-1])
   
        
