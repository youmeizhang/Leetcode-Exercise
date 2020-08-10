# credit to: https://leetcode.com/problems/largest-plus-sign/discuss/113319/Python-250ms-solution

class Solution(object):
    def orderOfLargestPlusSign(self, N, mines):
        """
        :type N: int
        :type mines: List[List[int]]
        :rtype: int
        """
        rows = [[-1, N] for _ in range(N)]
        cols = [[-1, N] for _ in range(N)]
        for r, c in mines:
            rows[r].append(c)
            cols[c].append(r)
        
        for i in range(N):
            rows[i].sort()
            cols[i].sort()
        
        res = 0
        for r in range(N):
            n = len(rows[r]) - 1
            for i in range(n):
                left_b = rows[r][i]
                right_b = rows[r][i+1]
                for c in range(left_b + res + 1, right_b - res):
                    idx = bisect_right(cols[c], r) - 1
                    up_b = cols[c][idx]
                    down_b = cols[c][idx+1]
                    res = max(res, min(c - left_b, right_b - c, r - up_b, down_b - r))
        return res
                
