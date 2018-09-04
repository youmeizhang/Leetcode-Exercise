
#error
class Solution:
    def updateMatrix(self, matrix):
        h = len(matrix)
        w = len(matrix[0])
        if h == 1:
            dp = [[0]]
        else:
            dp = [[max(h, w)] * w for x in range(h)]

        def dfs(x, y):
            for dx, dy in zip([1, 0, -1, 0], [0, 1, 0, -1]):
                nx = x + dx
                ny = y + dy

                if nx < 0 or ny < 0 or nx > h - 1 or ny > w - 1:
                    continue
                else:                
                    if matrix[x][y] == 0 and matrix[nx][ny] == 0:
                        dp[x][y] = min(dp[x][y], 0)

                    elif matrix[x][y] == 0 and matrix[nx][ny] == 1:
                        dp[x][y] = min(dp[x][y], 1)
                    elif matrix[x][y] == 1 and matrix[nx][ny] == 0:
                        dp[x][y] = min(dp[x][y], 1)

                    else:
                        dp[x][y] = min(dp[x][y], dp[nx][ny] + 1)


        for i in range(h):
            for j in range(w):
                dfs(i, j)

        return dp
