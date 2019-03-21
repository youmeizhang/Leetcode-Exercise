class Solution(object):
    def maxAreaOfIsland(self, grid):
        row = len(grid)
        column = len(grid[0])

        def dfs(i, j, row, column, grid):
            grid[i][j] = 0
            for dx, dy in zip([0,1,0,-1],[1,0,-1,0]):
                new_x = dx + i
                new_y = dy + j
                if new_x in range(0,row) and new_y in range(0, column) and grid[new_x][new_y] == 1:
                    self.count += 1
                    dfs(new_x, new_y, row, column, grid)
                    
        res = 0            
        for i in range(row):
            for j in range(column):
                if grid[i][j] == 1:
                    self.count = 1
                    dfs(i, j, row, column, grid)
                    res = max(res, self.count)

        return res
