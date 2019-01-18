class Solution(object):
    def findPaths(self, m, n, N, i, j):
        dp = [[[0] * n for _ in range(m)] for _ in range(N+1)]
        for k in range(1, N+1):
            for x in range(0, m):
                for y in range(0, n):

                    if x == 0:
                        v1 = 1
                    else:
                        v1 = dp[k-1][x-1][y]
                    if x == m - 1:
                        v2 = 1
                    else:
                        v2 = dp[k-1][x+1][y]
                    if y == 0:
                        v3 = 1
                    else:
                        v3 = dp[k-1][x][y-1]
                    if y == n - 1:
                        v4 = 1
                    else:
                        v4 = dp[k-1][x][y+1]
                    dp[k][x][y] = (v1 + v2 + v3 + v4) % 1000000007
        return dp[N][i][j]
