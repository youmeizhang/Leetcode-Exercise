
def pacificAtlantic(self, matrix):
    m = len(matrix)
    n = len(matrix[0]) if m else 0
    if m * n == 0: return []
    topEdge = [(0, y) for y in range(n)]
    leftEdge = [(x, 0) for x in range(m)]
    pacific = set(topEdge + leftEdge)
    
    bottomEdge = [(m-1, y) for y in range(n)]
    rightEdge = [(x, n-1) for x in range(m)]
    atlantic = set(bottomEdge + rightEdge)
    
    def bfs(vset):
        dz = zip([1, 0, -1, 0], [0, 1, 0, -1])
        queue = list(vset)
        while queue:
            hx, hy = queue.pop(0)
            for dx, dy in dz:
                nx, ny = hx + dx, hy + dy
                if 0 <= nx < m and 0 <= ny < n:
                    if matrix[nx][ny] >= matrix[hx][hy]:
                        if (nx, ny) not in vset:
                            queue.append((nx, ny))
                            vset.add((nx, ny))
    bfs(pacific)
    bfs(atlantic)
    result = pacific & atlantic
    return map(list, result)
    
#Solution with one problem
class Solution(object):
    def pacificAtlantic(self, matrix):
        h = len(matrix[0])
        w = len(matrix)

        dp = [[False for i in range(h)] for j in range(w)]
        for i in range(h):
            dp[0][i] = 1
        for j in range(w):
            dp[j][0] = 1

        dp2 = [[False for i in range(h)] for j in range(w)]
        for i in range(h):
            dp2[w-1][i] = 1
        for j in range(w):
            dp2[j][h-1] = 1

        def dfs(x, y):
            for dx, dy in zip([1, 0, -1, 0], [0, 1, 0, -1]):
                nx = x + dx
                ny = y + dy
                if 0 <= nx < h and 0 <= ny < w and matrix[nx][ny] <= matrix[x][y]:
                    if not dp[nx][ny]: dp[nx][ny] = dfs(nx, ny) #problem is here
                    if dp[nx][ny] == 1:
                        dp[x][y] = 1
            return dp[x][y]

        def dfs2(x, y):
            for dx, dy in zip([1, 0, -1, 0], [0, 1, 0, -1]):
                nx = x + dx
                ny = y + dy
                if 0 <= nx < h and 0 <= ny < w and matrix[x][y] >= matrix[nx][ny]:
                    if not dp2[nx][ny]: dp2[nx][ny] = dfs2(nx, ny) # problem here
                    if dp2[nx][ny] == 1:
                        dp2[x][y] = 1
            return dp2[x][y]

        for i in range(w):
            for j in range(h):
                if not dp[i][j]:
                    dp[i][j] = dfs(i, j)

        for i in reversed(range(w)):
            for j in reversed(range(h)):
                if not dp2[i][j]:
                    dp2[i][j] = dfs2(i, j)

        res = []
        for i in range(w):
            for j in range(h):
                if dp[i][j] == 1 and dp2[i][j] == 1:
                    res.append((i, j)) 

        return res
