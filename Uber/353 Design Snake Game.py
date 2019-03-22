class SnakeGame(object):

    def __init__(self, width, height, food):
        self.width = width
        self.height = height
        self.food = food
        self.x = 0
        self.y = 0
        self.i = 0
        self.score = 0
        self.body = [[0,0]]
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        

    def move(self, direction):
        if direction == "U":
            self.x -= 1
            
            if self.x in range(0, self.height) and self.y in range(0, self.width):
                if self.i < len(self.food) and self.x == self.food[self.i][0] and self.y == self.food[self.i][1]:
                    self.score += 1
                    self.i += 1
                    self.body.append([self.x, self.y])
                    
                    
                else:
                    self.body = self.body[1:] + [[self.body[-1][0] - 1, self.body[-1][1]]]  
                if self.body[-1] in self.body[:-1]:
                    return -1
                else:
                    return self.score
            else:
                return -1
            
        elif direction == "L":
            self.y -= 1
            if self.x in range(0, self.height) and self.y in range(0, self.width):
                if self.i < len(self.food) and self.x == self.food[self.i][0] and self.y == self.food[self.i][1]:
                    self.score += 1
                    self.i += 1
                    self.body.append([self.x, self.y])
                else:
                    self.body = self.body[1:] + [[self.body[-1][0], self.body[-1][1] - 1]]                    
                if self.body[-1] in self.body[:-1]:
                    return -1
                else:
                    return self.score
        
            else:
                return -1             
            
        elif direction == "D":
            self.x += 1
            if self.x in range(0, self.height) and self.y in range(0, self.width):
                if self.i < len(self.food) and self.x == self.food[self.i][0] and self.y == self.food[self.i][1]:
                    self.score += 1
                    self.i += 1
                    self.body.append([self.x, self.y])
                else:
                    self.body = self.body[1:] + [[self.body[-1][0]+1, self.body[-1][1]]]  
                    
                if self.body[-1] in self.body[:-1]:
                    return -1

                else:
                    return self.score
        
            else:
                return -1           
        else:
            self.y += 1
            if self.x in range(0, self.height) and self.y in range(0, self.width):
                if self.i < len(self.food) and self.x == self.food[self.i][0] and self.y == self.food[self.i][1]:
                    self.score += 1
                    self.i += 1
                    self.body.append([self.x, self.y])
                else:
                    self.body = self.body[1:] + [[self.body[-1][0], self.body[-1][1] + 1]]                    
                if self.body[-1] in self.body[:-1]:
                    return -1
                else:
                    return self.score
        
            else:
                return -1
