class FirstUnique:

    def __init__(self, nums: List[int]):
        n = len(nums)
        self.dic = {}
        for i in range(n):
            if nums[i] in self.dic:
                self.dic[nums[i]] += 1
            else:
                self.dic[nums[i]] = 1
        self.l = nums
        self.idx = 0

    def showFirstUnique(self) -> int:        
        while self.idx < len(self.l):
            if self.dic[self.l[self.idx]] == 1:
                return self.l[self.idx]
            else:
                self.idx += 1
        
        return -1

    def add(self, value: int) -> None:
        if value in self.dic:
            self.dic[value] += 1
        else:
            self.dic[value] = 1
        
        self.l.append(value)
        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
