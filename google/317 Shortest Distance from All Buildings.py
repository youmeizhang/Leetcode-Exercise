#credit to: https://github.com/jzysheep/LeetCode/blob/master/317.%20Shortest%20Distance%20from%20All%20Buildings.cpp

class Solution(object):
    def shortestDistance(self, grid):
        row = len(grid)
        if row == 0:
            return 0
        column = len(grid[0])

        building = 0
        for i in range(row):
            for j in range(column):
                if grid[i][j] == 1:
                    building += 1

        hit = [[0] * column for _ in range(row)]
        distSum = [[0] * column for _ in range(row)]

        def dfs(x, y, grid, hit, distSum, building, row, column):
            visited = [[False] * column for _ in range(row)]
            visited[x][y] = True
            countOne = 1
            dist = 0
            queue = [(x, y)]

            while queue:
                dist += 1
                levelCount = len(queue)
                for k in range(levelCount):

                    point = queue.pop(0)
                    x = point[0]
                    y = point[1]
                    for dx, dy in zip([0,1,0,-1], [1,0,-1,0]):
                        new_x = x + dx
                        new_y = y + dy
                        if new_x >= 0 and new_x < row and new_y >= 0 and new_y < column and not visited[new_x][new_y]:
                            visited[new_x][new_y] = True
                            if grid[new_x][new_y] == 1:
                                countOne += 1
                            elif grid[new_x][new_y] == 0:
                                queue.append((new_x, new_y))
                                hit[new_x][new_y] += 1
                                distSum[new_x][new_y] += dist

            return countOne == building

        for i in range(row):
            for j in range(column):
                if grid[i][j] == 1:
                    if not dfs(i, j, grid, hit, distSum, building, row, column):
                        return -1

        res = float('inf')
        for i in range(row):
            for j in range(column):
                if grid[i][j] == 0 and hit[i][j] == building:
                    res = min(res, distSum[i][j])

        return res if res != float('inf') else -1
        
