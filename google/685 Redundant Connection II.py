#credit to: http://zxi.mytechroad.com/blog/graph/leetcode-685-redundant-connection-ii/

class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        def isCycle(v, p): 
            u = p[v]
            while u != 0:
                if u == v: 
                    return True
                u = p[u]
            return False
        
        p = [0] * (len(edges) + 1)
        ans1 = []
        ans2 = []
        dup_p = False
        
        for edge in edges:
            u, v = edge
            if p[v] > 0:
                ans1 = [p[v], v]
                ans2 = [u,v]
                dup_p = True
                edge[0] = edge[1] = -1
            else:
                p[v] = u
        p = [0] * (len(edges) + 1)
        
        for u, v in edges:
            if u < 0:
                continue
            p[v] = u
            if isCycle(v, p):
                return ans1 if dup_p else [u,v]
        return ans2
            
