class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        row = len(board)
        if row > 0:
            col = len(board[0])
            self.visited = [[False] * col for _ in range(row)]
        
        def dfs(x, y):
            self.visited[x][y] = True
            for dx, dy in zip([0,1,0,-1],[1,0,-1,0]):
                new_x = dx + x
                new_y = dy + y
                if new_x in range(row) and new_y in range(col) and not self.visited[new_x][new_y] and board[new_x][new_y] == "O":

                    if new_x == 0 or new_x == row - 1 or new_y == 0 or new_y == col - 1:
                        self.flag = True
                    else:
                        self.region.append([new_x, new_y])
                        dfs(new_x, new_y)
                        
        res = []
        if row > 0 and col > 0:
            for i in range(row):
                for j in range(col):
                    if i in range(1, row-1) and j in range(1, col-1) and not self.visited[i][j] and board[i][j] == "O":
                        self.region = [[i, j]]
                        self.flag = False
                        dfs(i, j)
                        if self.flag:
                            continue
                        res += self.region
                       
        for pair in res:
            board[pair[0]][pair[1]] = "X"
        
            
