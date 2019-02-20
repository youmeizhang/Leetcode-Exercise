import copy

class Solution(object):

    def check_rotten(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return False
        return True

    def orangesRotting(self, grid):
        row = len(grid)
        column = len(grid[0])
        count = 0
        prev_grid = copy.deepcopy(grid)

        while True:
            if self.check_rotten(grid):
                break
            for i in range(row):
                for j in range(column):
                    if grid[i][j] != 1:
                        continue
                    rot = False
                    for dx, dy in zip([0,1,0,-1], [1,0,-1,0]):
                        x = i + dx
                        y = j + dy
                        if x < 0 or y < 0 or x >= row or y >= column:
                            continue
                        if prev_grid[x][y] == 2:
                            rot = True
                            break
                    if rot:
                        grid[i][j] = 2
            count += 1
            if grid == prev_grid:
                break
            prev_grid = copy.deepcopy(grid)
        if self.check_rotten(grid):
            return count
        return -1
