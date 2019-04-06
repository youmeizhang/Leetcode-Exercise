#credit to: https://blog.csdn.net/weixin_41677877/article/details/82599635

class Solution(object):
    def validTree(self, n, edges):
        root = [i for i in range(n)]
        for i in edges:
            root1 = self.findTree(root, i[0])
            root2 = self.findTree(root, i[1])
            if root1 == root2:
                return False
            root[root2] = root1
        return len(edges) == n-1
        
    def findTree(self, root, n):
        if root[n] == n:
            return n
        return self.findTree(root, root[n])
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        
