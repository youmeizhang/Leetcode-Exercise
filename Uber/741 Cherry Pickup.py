# credit to: https://www.youtube.com/watch?v=vvPSWORCKow

class Solution(object):
    def cherryPickup(self, grid):
        n = len(grid)
        grid_ = copy.deepcopy(grid)
        m_ = [[[float('-inf')] * n for _ in range(n)] for _ in range(n)]

        def dp(x1, y1, x2):
            y2 = x1 + y1 - x2
            if x1 < 0 or y1 < 0 or x2 < 0 or y2 < 0:
                return -1
            if grid_[y1][x1] < 0 or grid_[y2][x2] < 0:
                return -1
            if x1 == 0 and y1 == 0:
                return grid_[y1][x1]
            if m_[x1][y1][x2] != float('-inf'):
                return m_[x1][y1][x2]
            ans = max(dp(x1-1, y1, x2-1), dp(x1, y1-1, x2), dp(x1, y1-1,x2-1), dp(x1-1, y1, x2))
            if ans < 0:
                m_[x1][y1][x2] = -1
                return m_[x1][y1][x2]
            ans += grid_[y1][x1]
            if x1 != x2:
                ans += grid_[y2][x2]
            m_[x1][y1][x2] = ans
            return m_[x1][y1][x2]

        return max(0, dp(n-1, n-1, n-1))
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
