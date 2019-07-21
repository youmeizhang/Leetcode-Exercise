# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
            
        def helper(nums):
            if not nums:
                return
            n = len(nums)
            mid = n // 2
            root = TreeNode(nums[mid])
            root.left = helper(nums[:mid])
            root.right = helper(nums[mid+1:])
        
            return root
        return helper(nums)
