class Solution(object):
    def candyCrush(self, board):
        row = len(board)
        col = len(board[0])
        
        def check(i, j):
            if i in range(row) and j in range(col):
                return True
            return False

        def dfs1(i, j):
            self.visited[i][j] = True
            for dx, dy in zip([-1, 1], [0, 0]):
                x = dx + i
                y = dy + j
                if check(x, y) and board[x][y] == self.value and not self.visited[x][y]:
                    self.count1 += 1
                    self.pos1.append([x, y])
                    dfs1(x, y)
                    
        def dfs2(i, j):
            
            self.visited2[i][j] = True
            for dx, dy in zip([0, 0], [1, -1]):
                new_x = dx + i
                new_y = dy + j
                if check(new_x, new_y) and board[new_x][new_y] == self.value and not self.visited2[new_x][new_y]:
                    self.count2 += 1
                    self.pos2.append([new_x, new_y])
                    dfs2(new_x, new_y)
                    
                    
        total_pos = []
          
        def checkBoard():
            for i in range(row):
                for j in range(col):
                    self.count1 = 1
                    self.value = board[i][j]
                    self.visited = [[False] * col for _ in range(row)]
                    self.pos1 = [[i, j]]
                    if self.value != 0:
                        dfs1(i, j)
                    if self.count1 >= 3:
                        for pos in self.pos1:
                            if pos in total_pos:
                                continue
                            else:
                                total_pos.append(pos)

                    self.visited2 = [[False] * col for _ in range(row)]
                    self.count2 = 1
                    self.pos2 = []
                    if self.value != 0:
                        dfs2(i, j)
                    if self.count2 >= 3:
                        for pos in self.pos2:
                            if pos in total_pos:
                                continue
                            else:
                                total_pos.append(pos)

            for p in range(len(total_pos)):
                x, y = total_pos[p]
                board[x][y] = 'del'
            
        
        def changeBoard():
            for m in range(row-1, -1, -1):
                b = m - 1
                for n in range(col):
                    b = m - 1
                    if board[m][n] == 'del':
                        while b >= 0 and board[b][n] == 'del':
                            b -= 1

                        if b >= 0:
                            board[m][n] = board[b][n]
                            board[b][n] = 'del'
                            b -= 1

                        else:
                            board[m][n] = 0
            
        while True:
            checkBoard()
            if total_pos != []:
                changeBoard()
            else:
                break
            total_pos = []
        return board

# credit to: http://www.cnblogs.com/lightwindy/p/9744174.html
class Solution(object):
    def candyCrush(self, board):
        row = len(board)
        col = len(board[0])

        flag = True
        while flag:
            flag = False

            for r in range(row):
                for c in range(col - 2):
                    if abs(board[r][c]) == abs(board[r][c+1]) == abs(board[r][c+2]) != 0:
                        board[r][c] = board[r][c+1] = board[r][c+2] = -abs(board[r][c])
                        flag = True


            for r in range(row - 2):
                for c in range(col):
                    if abs(board[r][c]) == abs(board[r+1][c]) == abs(board[r+2][c]) != 0:
                        board[r][c] = board[r+1][c] = board[r+2][c] = -abs(board[r][c])
                        flag = True
      
            for c in range(col):
                i = row - 1
                for r in reversed(range(row)):
                    if board[r][c] > 0:
                        #replace the original value with only positive value
                        board[i][c] = board[r][c]
                        i -= 1

                for r in reversed(range(i+1)):
                    board[r][c] = 0
        return board
