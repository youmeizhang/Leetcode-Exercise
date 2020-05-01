class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        def tranverse(root, i):
            if not root:
                return
            if i < len(arr) and root.val == arr[i]:
                if i == len(arr) - 1 and root.left is None and root.right is None:
                    return True
                else:
                    return tranverse(root.left, i+1) or tranverse(root.right, i+1)
        return tranverse(root, 0)
