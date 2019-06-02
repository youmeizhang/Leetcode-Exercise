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
        
