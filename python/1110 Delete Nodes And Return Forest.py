# credit to: https://leetcode.com/problems/delete-nodes-and-return-forest/discuss/328853/JavaPython-Recursion-Solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        res = []
        to_delete = set(to_delete)
        
        def helper(root, is_root):
            if not root:
                return None
            root.left = helper(root.left, root.val in to_delete)
            root.right = helper(root.right, root.val in to_delete)
            if root.val not in to_delete and is_root:
                res.append(root)
            return None if root.val in to_delete else root
        
        helper(root, True)
        return res
            
