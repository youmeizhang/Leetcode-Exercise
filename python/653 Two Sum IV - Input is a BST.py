class Solution:
    def findTarget(self, root, k):
        self.dic = collections.defaultdict(int)
        self.l = []
        self.res = False
        def tranverse(root, k):
            if not root:
                return
            
            self.dic[root.val] += 1
            self.l.append(root.val)
            
            if k - root.val == root.val:
                if self.dic[root.val] > 1:
                    self.res = True
                    return
            
            else:
                if self.dic[k - root.val] > 0:
                    self.res = True
                    return
            
            tranverse(root.left, k)
            tranverse(root.right, k)
                
        tranverse(root, k)
        
        return self.res
