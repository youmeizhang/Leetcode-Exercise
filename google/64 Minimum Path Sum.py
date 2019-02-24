class Solution(object):
    def minPathSum(self, grid):
        row = len(grid)
        column = len(grid[0])

        for i in range(row):
            for j in range(column):
                if i == 0 and j == 0:
                    previous = 0
                elif i == 0:
                    previous = grid[0][j-1]
                elif j == 0:
                    previous = grid[i-1][j]
                else:
                    previous = min(grid[i-1][j], grid[i][j-1])
                grid[i][j] = previous + grid[i][j]

        return grid[-1][-1]
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
