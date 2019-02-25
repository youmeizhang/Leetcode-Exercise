class TicTacToe(object):

    def __init__(self, n):
        self.grid = [["-"] * n for _ in range(n)]
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diag = [0] * n
        self.rediag = [0] * n
        
        """
        Initialize your data structure here.
        :type n: int
        """
        

    def move(self, row, col, player):
        if player == 1:
            self.rows[row] += 1
            self.cols[col] += 1
            if row == col:
                self.diag[row] += 1
            if row + col == self.n-1:
                self.rediag[row] += 1
            
        elif player == 2:
            self.rows[row] -= 1
            self.cols[col] -= 1
            if row == col:
                self.diag[row] -= 1
            if row + col == self.n - 1:
                self.rediag[row] -= 1
        
        if max(self.rows) == self.n or max(self.cols) == self.n or sum(self.diag) == self.n or sum(self.rediag) == self.n:
            return player
        elif min(self.rows) == -1 * self.n or min(self.cols) == -1 * self.n or sum(self.diag) == -1 * self.n or sum(self.rediag) == -1 * self.n:
            return player
        else:
            return 0
        
#solution 2:
class TicTacToe(object):

    def __init__(self, n):
        self.grid = [["-"] * n for _ in range(n)]
        self.n = n
        """
        Initialize your data structure here.
        :type n: int
        """
        

    def move(self, row, col, player):
        self.grid[row][col] = player

        #check right, j += 1
        count = 0
        for j in range(self.n):
            if self.grid[row][j] == player:
                count += 1
        if count == self.n:
            return player
        
        #check up, i -= 1
        count = 0
        for i in range(self.n):
            if self.grid[i][col] == player:
                count += 1
        if count == self.n:
            return player
        
        #check diagonal, i += 1, j -= 1
        count = 0
        i = 0
        j = self.n - 1
        while i < self.n and j >= 0:
            if self.grid[i][j] == player:
                count += 1
            i += 1
            j -= 1
        if count == self.n:
            return player
        
        #check diagonal, i += 1, j += 1
        count = 0
        i = 0
        j = 0
        while i < self.n and j < self.n:
            if self.grid[i][j] == player:
                count += 1
            i += 1
            j += 1
            
        if count == self.n:
            return player
        
        return 0
                
            
            
                
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
