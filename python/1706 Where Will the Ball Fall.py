class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        row = len(grid)
        col = len(grid[0])

        res = [0] * col
        
        def helper(x, y):
            if grid[x][y] == 1:
                # look at right side
                if y < col - 1 and grid[x][y+1] == 1:
                    if x == row - 1:
                        return y+1
                    else:
                        return helper(x+1, y+1)
                else:
                    return -1
            else:
                # look at left side
                if y > 0 and grid[x][y-1] == -1:
                    if x == row - 1:
                        return y-1
                    else:
                        return helper(x+1, y-1)
                else:
                    return -1
        res = []
        for i in range(col):
            res.append(helper(0, i))
        return res
                
                    
        
