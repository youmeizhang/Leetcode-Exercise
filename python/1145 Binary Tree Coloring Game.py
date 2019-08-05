# credit to:https://leetcode.com/problems/binary-tree-coloring-game/discuss/350570/JavaC%2B%2BPython-Simple-recursion-and-Follow-Up

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        cnt = [0, 0]
        
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            if root.val == x:
                cnt[0], cnt[1] = left, right
            return left + right + 1
        dfs(root)
        print(cnt)
        return max(max(cnt), n - sum(cnt) - 1) > n / 2
        
        
        
