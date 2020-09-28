class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        row = len(grid)
        col = len(grid[0])
        
        m_ = [[[-1] * col for _ in range(col)] for _ in range(row)]
        
        def dp(y, x1, x2):
            if y not in range(0, row) or x1 not in range(0, col) or x2 not in range(0, col):
                return 0

            ans = m_[y][x1][x2]
            if ans != -1:
                return ans
            
            cur = grid[y][x1]
            if x1 != x2:
                cur += grid[y][x2]
                
            for i in [-1,0,1]:
                for j in [-1,0,1]:
                    ans = max(ans, cur + dp(y+1, x1+i, x2+j))
            
            m_[y][x1][x2] = ans
            return m_[y][x1][x2]
            
            
        return dp(0, 0, col - 1)
        
