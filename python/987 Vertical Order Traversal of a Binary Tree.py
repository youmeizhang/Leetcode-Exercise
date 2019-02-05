class Solution:
    def verticalTraversal(self, root: 'TreeNode') -> 'List[List[int]]':

        dic = collections.defaultdict(list)
        
        def tranverse(root, start, end):
            if root is not None:
                
                dic[start].append((end, root.val))

                tranverse(root.left, start - 1, end + 1)
                tranverse(root.right, start + 1, end + 1)
            
        
        tranverse(root, 0, 0)
        for key in dic:
            dic[key].sort()
            
        ks = dic.keys()
        ks = sorted(ks)
        
        return [[s[1] for s in dic[key]] for key in ks]
