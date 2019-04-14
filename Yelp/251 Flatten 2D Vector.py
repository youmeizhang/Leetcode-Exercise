class Vector2D(object):

    def __init__(self, v):
        
        self.row = 0
        self.col = 0
        self.v = v
        
        while self.row != len(self.v):
            if len(self.v[self.row]) != 0:
                self.col = 0
                break
            self.row += 1
        """
        :type v: List[List[int]]
        """
        

    def next(self):
        print(self.row, self.col)
        ret = self.v[self.row][self.col]
        self.col += 1
        if self.col == len(self.v[self.row]):
            self.col = 0
            self.row += 1
        return ret
            
        
        
        """
        :rtype: int
        """
        

    def hasNext(self):
        if self.row == len(self.v):
            return False
        if self.col != len(self.v[self.row]):
            return True
        else:
            self.row += 1
            while self.row != len(self.v):
                if len(self.v[self.row]) != 0:
                    self.col = 0
                    return True
            
                self.row += 1
            return False
        """
        :rtype: bool
        """
        


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()
