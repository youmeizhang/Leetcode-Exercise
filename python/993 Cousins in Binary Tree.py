#credit to: lihuoran

class Solution(object):
        
    def isCousins(self, root, x, y):
        
        def dfs(root, lev, pare):
            if not root:
                return
            self.level[root.val] = lev
            self.parent[root.val] = pare
            dfs(root.left, lev + 1, root.val)
            dfs(root.right, lev + 1, root.val)
            
        self.level = {}
        self.parent = {}
        
        dfs(root, 0, -1)
        return (self.level[x] == self.level[y]) and (self.parent[x] != self.parent[y])

