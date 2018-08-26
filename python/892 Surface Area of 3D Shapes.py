#credit to: fuxuemingzhu 
class Solution:
    def surfaceArea(self, grid):
        n = len(grid)
        res = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    res += grid[i][j] * 4 + 2
                if i: res -= min(grid[i - 1][j], grid[i][j]) * 2
                if j: res -= min(grid[i][j - 1], grid[i][j]) * 2
        return res
        
