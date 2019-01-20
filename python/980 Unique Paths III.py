class Solution(object):
    def uniquePathsIII(self, grid):
        row = len(grid)
        column = len(grid[0])
        visited = [[False] * column for i in range(row)]
        self.res = 0
        empty = set()
        
        for i in range(row):
            for j in range(column):
                if grid[i][j] == 1:
                    start = [i, j]
                elif grid[i][j] == 0:
                    empty.add((i,j))
                    
        def check(i, j):
            if i >= row or j >= column or i < 0 or j < 0 or grid[i][j] == -1:
                return False
            return True
        
        def dfs(i, j, visited, count):
            if (i, j) in visited:
                return
            
            if not check(i, j):
                return
            
            if grid[i][j] == 2:
                if count == len(empty):
                    self.res += 1
                return
            
            if grid[i][j] == 0:
                count += 1

            visited.add((i,j))
            
            dfs(i+1, j, set(k for k in visited), count)
            dfs(i-1, j, set(k for k in visited), count)
            dfs(i, j+1, set(k for k in visited), count)
            dfs(i, j-1, set(k for k in visited), count)    
                 
        dfs(start[0], start[1], set(), 0)  
        
        return self.res
