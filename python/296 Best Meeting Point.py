class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        r = []
        c = []
        
        for x in range(row):
            for y in range(col):
                if grid[x][y] == 1:
                    r.append(x)
                    c.append(y)
                    
        r = sorted(r)
        c = sorted(c)
        
        n = len(r)
        
        if n % 2 == 1:
            mid_r = r[n // 2]
            mid_c = c[n // 2]
            
        else:
            mid_r = (r[n // 2] + r[n // 2 - 1]) // 2
            mid_c = (c[n // 2] + c[n // 2 - 1]) // 2
            
        dis = 0

        for i in range(n):
            tmp = abs(r[i] - mid_r) + abs(c[i] - mid_c)
            
            dis += tmp
            
        return dis
            
