class Solution(object):
    def minPathSum(self, grid):
        row = len(grid)
        column = len(grid[0])
        
        dp = [[0 for i in range(column)] for i in range(row)]
        dp[0][0] = grid[0][0]
        
        for i in range(1, column):
            dp[0][i] = dp[0][i-1] + grid[0][i]
        for i in range(1, row):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for i in range(1, row):
            for j in range(1, column):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[row-1][column-1]

# DFS
class Solution(object):
    def minPathSum(self, grid):
        self.res = float('inf')
        self.row = len(grid)
        self.column = len(grid[0])
        
        def dfs(x, y, visited, total):
            for dx, dy in zip([0, 1], [1, 0]):
                x = x + dx
                y = y + dy
                
                if x in range(0, self.row)and y in range(0, self.column) and not visited[x][y]:
                    visited[x][y] = True
                    total += grid[x][y]
                    if x == self.row - 1 and y == self.column - 1:
                        self.res = min(self.res, total)
                    else:
                        dfs(x, y, visited, total)
                    
        visited = [[False for i in range(self.column)] for i in range(self.row)]
        dfs(0, 0, visited, grid[0][0])
        return self.res
