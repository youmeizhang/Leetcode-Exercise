# credit to: http://bookshadow.com/weblog/2017/09/24/leetcode-redundant-connection/

class Solution(object):
    def findRedundantConnection(self, edges):

        parent = list(range(max(reduce(operator.add, edges)) + 1))        
        def find(a):
            while parent[a] != a:
                a = parent[a]
            return a

        for u, v in edges:
            pu = find(u)
            pv = find(v)
            if pu == pv:
                return [u,v]
            parent[pu] = pv
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """

# Original Union Find method
class UnionFindSet:
    def __init__(n):
        self.parents = [0] * (n+1)
        self.ranks = [0] * (n+1)
        for i in range(n+1):
            self.parents[i] = i        
    
    def union(x, y):
        px = find(x)
        py = find(y)
        if px == py:
            # no need to merge
            return False
        
        if self.ranks[px] > self.ranks[py]:
            self.parents[py] = px
        elif self.ranks[py] > self.ranks[px]:
            self.parents[px] = py
        else:
            self.parents[py] = px
            self.ranks[px] += 1
        return True
    
    def find(x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents(x))
        return self.parents[x]
    
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        UnionFindSet(n)
        
        for edge in edges:
            if not self.
        
    

