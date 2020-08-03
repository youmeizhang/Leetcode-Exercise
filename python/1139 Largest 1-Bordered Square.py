# credit to: https://leetcode.com/problems/largest-1-bordered-square/discuss/345265/c%2B%2B-beats-100-(both-time-and-memory)-concise-with-algorithm-and-image

class Solution(object):
    def largest1BorderedSquare(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])
        res = 0
        
        hor = [[0] * col for _ in range(row)]
        ver = [[0] * col for _ in range(row)]
        
        for i in range(row):
            total = 0
            for j in range(col):
                if grid[i][j] == 1:
                    total += 1
                    hor[i][j] = total
                else:
                    total = 0
                    hor[i][j] = total
        
        for j in range(col):
            total = 0
            for i in range(row):
                if grid[i][j] == 1:
                    total += 1  
                    ver[i][j] = total
                else:
                    total = 0
                    ver[i][j] = total
        
        res = 0
        max_ = 0
        for i in range(row-1, -1, -1):
            for j in range(col-1, -1, -1):
                min_ = min(hor[i][j], ver[i][j])
                while min_ > max_:
                    if hor[i-min_+1][j] >= min_ and ver[i][j-min_+1] >= min_:
                        max_ = min_
                    min_ -= 1
        return max_ * max_
                
                
                
        
