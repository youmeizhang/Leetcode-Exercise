class Solution(object):
    def find_parent(self, parent,i): 
        if parent[i] == -1: 
            return i 
        else:
            root = self.find_parent(parent, parent[i]) 
            parent[i] = root
            return root

        
    def findRedundantConnection(self, edges):
        parent = [-1] * (len(edges) + 1) 
        
        for edge in edges:
            a = self.find_parent(parent, edge[0])
            b = self.find_parent(parent, edge[1])
            if a != b:
                parent[a] = b
            else:
                return edge
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        
