class Solution:
    def verticalTraversal(self, root: 'TreeNode') -> 'List[List[int]]':

        self.dic = collections.defaultdict(int)
        self.pos = [0, 0]
        
        def tranverse(root, start, end):
            if not root:
                return

            if self.dic[start] == 0:
                self.dic[start] = [root.val]
            else:
                self.dic[start].append(root.val)

            tranverse(root.left, start - 1, end - 1)
            tranverse(root.right, start + 1, end - 1)
        res = []
        tranverse(root, 0, 0)
        for key, value in sorted(self.dic.items()):
            res.append(value)

        return res
