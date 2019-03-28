class Solution(object):
    def shortestBridge(self, A):
        row = len(A)
        column = len(A[0])
        self.queue = collections.deque()
        
        def dfs(i, j):
            A[i][j] = 'X'
            for dx, dy in zip([0,1,0,-1],[1,0,-1,0]):
                x = dx + i
                y = dy + j
                if x in range(0, row) and y in range(0, column) and A[x][y] == 1:
                    A[x][y] = 'X'                  
                    self.queue.append((x,y))
                    dfs(x, y)
        flag = False
        for i in range(row):
            for j in range(column):
                if A[i][j] == 1: 
                    self.queue.append((i,j))
                    dfs(i, j)
                    flag = True
                    break
            if flag:
                break
        
        self.dist = 0
        while self.queue:
            size = len(self.queue)
            for _ in range(size):
                x, y = self.queue.popleft()
                for dx, dy in zip([0,1,0,-1],[1,0,-1,0]):
                    newx = x + dx
                    newy = y + dy
                    if newx in range(0, row) and newy in range(0, column):                
                        if A[newx][newy] == 0:
                            A[newx][newy] = 'X'
                            self.queue.append((newx, newy))

                        elif A[newx][newy] == 1:
                            return self.dist
                        else:
                            continue
            self.dist += 1
            
        return -1
