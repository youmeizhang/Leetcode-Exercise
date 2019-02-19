class Solution(object):
    def orangesRotting(self, grid):
        row = len(grid)
        column = len(grid[0])

        def dfs(i, j, row, column, grid, count):
            for dx, dy in zip([0,1,0,-1],[1,0,-1,0]):
                new_i = i + dx
                new_j = j + dy
                if new_i >= 0 and new_i < row and new_j >= 0 and new_j < column and grid[i][j] == 2:
                    if grid[new_i][new_j] == 1:
                        grid[new_i][new_j] = 2
                        count = 1
                        #print(grid)
                    else:
                        continue
            return count

        count = 0
        tmp = 0
        res = 0
        for i in range(row):
            for j in range(column):
                res += dfs(i, j, row, column, grid, count)

        for i in range(row):
            for j in range(column):
                if grid[i][j] == 1:
                    return -1
        return res
