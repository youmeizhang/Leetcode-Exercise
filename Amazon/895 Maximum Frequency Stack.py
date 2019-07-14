class FreqStack:

    def __init__(self):
        self.stack = []
        self.dic = {}
        self.index = 0
        

    def push(self, x: int) -> None:
        if x in self.dic:
            self.dic[x] += 1
        else:
            self.dic[x] = 1
            
        heapq.heappush(self.stack, (-1 * self.dic[x], -1 * self.index, x))
        self.index += 1
     
    def pop(self) -> int:
        res = heapq.heappop(self.stack)
        self.dic[res[2]] -= 1
        return res[2]
        
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
