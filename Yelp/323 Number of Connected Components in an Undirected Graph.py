# credit to: https://www.youtube.com/watch?v=Mf5lJvvYa3Q

class Solution(object):
    def countComponents(self, n, edges):
        roots = [-1] * n
        res = n
        for n1, n2 in edges:
            x = self.find(roots, n1)
            y = self.find(roots, n2)
            if x != y:
                roots[x] = y
                res -= 1
        return res
        
    def find(self, roots, i):
        while roots[i] != -1:
            i = roots[i]
        return i
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        
