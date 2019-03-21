class Solution(object):
    def wallsAndGates(self, rooms):
        row = len(rooms)
        column = len(rooms[0]) if row != 0 else 0
        
        def dfs(i, j, row, column, dist):
            for dx, dy in zip([0,1,0,-1], [1,0,-1,0]):
                new_x = dx + i
                new_y = dy + j
                if new_x in range(0, row) and new_y in range(0, column) and rooms[new_x][new_y] > dist:
                    rooms[new_x][new_y] = dist
                    dfs(new_x, new_y, row, column, dist + 1)
                else:
                    continue

        for i in range(row):
            for j in range(column):
                if rooms[i][j] == 0:
                    dfs(i, j, row, column, 1)
                    
        
# Time Limit
class Solution(object):
    def wallsAndGates(self, rooms):
        self.rooms = rooms
        row = len(self.rooms)
        column = len(self.rooms[0]) if row != 0 else 0

        def check(i, j, row, column):
            if i >= 0 and j >= 0 and i < row and j < column and self.rooms[i][j] != -1 and self.rooms[i][j] != 0:
                return True
            return False

        def dfs(i, j, row, column, visited, dist):
            visited[i][j] = True
            for dx, dy in zip([0,1,0,-1], [1,0,-1,0]):
                new_x = dx + i
                new_y = dy + j
                if check(new_x, new_y, row, column) and self.rooms[new_x][new_y] > dist:
                    self.rooms[new_x][new_y] = min(self.rooms[new_x][new_y], dist)
                    dfs(new_x, new_y, row, column, visited, dist + 1)
                else:
                    continue

        for i in range(row):
            for j in range(column):
                visited = [[False] * column for _ in range(row)]
                if self.rooms[i][j] == 0:
                    dfs(i, j, row, column, visited, 1)
