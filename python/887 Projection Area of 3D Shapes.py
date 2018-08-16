class Solution:
    def projectionArea(self, grid):
        x = len(grid)
        y = len(grid[0])
        
        tmp = 0
        for i in grid:
            for j in i:
                if j == 0:
                    tmp += 1
        
        sum1 = x * y - tmp
        
        sum2 = 0
        for i in grid:
            if max(i) != 0:
                sum2 += max(i)
            else:
                continue
                
        sum3 = 0
        tmp3 = []
        for j in range(y):
            for i in range(x):
                tmp3.append(grid[i][j])
            sum3 += max(tmp3)
            tmp3 = []
        
        return sum1+sum2+sum3
