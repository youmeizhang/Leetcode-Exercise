class Solution:
    def findDuplicateSubtrees(self, root):
        dic = collections.defaultdict(int)
        res = []
        
        self.postorder(root, dic, res)
        return res
    
    def postorder(self, root, dic, res):
        if not root:
            return "#"
        path = str(root.val) + "," + self.postorder(root.left, dic, res) + "," + self.postorder(root.right, dic, res)
        if dic[path] == 1:
            res.append(root)
        dic[path] += 1
        return path
