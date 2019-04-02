#credit to: https://redtongue.coding.me/2019/03/31/1020-Number-of-Enclaves/
class Solution(object):
    def numEnclaves(self, A):
        row = len(A)
        column = len(A[0])
        
        def check(i, j):
            if i < row and i >= 0 and j < column and j >= 0:
                return True
            return False
        
        def dfs(i, j):
            if check(i, j) and A[i][j] == 1:
                A[i][j] = 0
                dfs(i+1, j)
                dfs(i, j+1)
                dfs(i-1, j)
                dfs(i, j-1)
            
        for i in [0, row-1]:
            for j in range(column):
                if A[i][j]:
                    dfs(i, j)
                    
        for i in range(row):
            for j in [0, column-1]:
                if A[i][j]:
                    dfs(i, j)
                    
        return sum([sum(a) for a in A])                    

# with one bug, unsure why
class Solution(object):
    def numEnclaves(self, A):
        row = len(A)
        column = len(A[0])
        self.enclaves = []
        self.count = 0
        
        def dfs(i, j, visited):
            visited[i][j] = True
            for dx, dy in zip([0,1,0,-1], [1,0,-1,0]):
                x = dx + i
                y = dy + j
                
                if (x == 0 or y == 0 or x == row - 1 or y == column - 1) and x in range(row) and y in range(column) and A[x][y] == 1:
                    self.enclaves.append([i, j])
                    return True
                elif [x, y] in self.enclaves: 
                    self.enclaves.append([i, j])
                    return True
                
                elif x in range(0, row) and y in range(0, column) and A[x][y] == 1:
                    if not visited[x][y]:
                        if dfs(x, y, visited):
                            self.enclaves.append([i, j])
            return False
            
        for i in range(row):
            for j in range(column):
                visited = [[False] * column for _ in range(row)]
                if A[i][j] == 1:
                    if dfs(i, j, visited):

                        self.enclaves.append([i, j])
                        for dx, dy in zip([0,1,0,-1], [1,0,-1,0]):
                            x = dx + i
                            y = dy + j
                            if x in range(row) and y in range(column) and A[x][y] == 1:
                                self.enclaves.append([x, y])

        for i in range(1, row - 1):
            for j in range(1, column - 1):
                if A[i][j] == 1 and [i, j] not in self.enclaves:
                    self.count += 1

        return self.count
