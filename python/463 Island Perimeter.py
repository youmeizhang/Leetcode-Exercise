class Solution(object):
    def islandPerimeter(self, grid):
        res = 0
        h = len(grid)
        w = len(grid[0]) if h else 0

        for i in range(h):
            for j in range(w):
                if grid[i][j] == 1:
                    res += 4
                    if i > 0 and grid[i-1][j]:
                        res -= 2
                    if j > 0 and grid[i][j-1]:
                        res -= 2
        return res
