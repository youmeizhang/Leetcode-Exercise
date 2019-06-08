# credit to: https://leetcode.com/problems/campus-bikes-ii/discuss/307544/dfs-with-memorization

class Solution(object):
    def assignBikes(self, workers, bikes):
        def dist(i, j):
            return abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1])

        w = len(workers)
        b = len(bikes)
        memo = {}
        visited = [False] * b

        def dfs(i):
            if i == w:
                return 0
            res = float('inf')
            for j in range(b):
                if not visited[j]:
                    visited[j] = True
                    tmp = tuple(visited)
                    if tmp not in memo:
                        memo[tmp] = dfs(i+1)
                    res = min(res, dist(i,j) + memo[tmp])
                    visited[j] = False
            return res
        return dfs(0)
        """
        :type workers: List[List[int]]
        :type bikes: List[List[int]]
        :rtype: int
        """
