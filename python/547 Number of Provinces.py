class UnionFindSet:
    def __init__(self, n):
        self.parents = [0] * (n+1)
        self.ranks = [0] * (n+1)
        for i in range(n+1):
            self.parents[i] = i        
    
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            # no need to merge
            return
        
        if self.ranks[px] > self.ranks[py]:
            self.parents[py] = px
        elif self.ranks[py] > self.ranks[px]:
            self.parents[px] = py
        else:
            self.parents[py] = px
            self.ranks[px] += 1
        return
    
    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        row = len(isConnected)
        col = len(isConnected[0])
        
        unionFind = UnionFindSet(row)
        for i in range(row):
            for j in range(col):
                if j > i and isConnected[i][j]:
                    unionFind.union(i+1, j+1)
                else:
                    continue
                    
        res = set()
        for i in range(col+1):
            res.add(unionFind.find(i))
        return len(res)-1
        

        
