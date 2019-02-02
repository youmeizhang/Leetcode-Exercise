class Solution:
    def constructMaximumBinaryTree(self, nums):
        self.root = None
        
        def recursive(nums, root):
            if not root:
                if nums:
                    root = TreeNode(max(nums))
                    
                if not nums:
                    return root
                
            root.left = recursive(nums[:nums.index(max(nums))], root.left)
            root.right = recursive(nums[nums.index(max(nums)) + 1: ], root.right)
            return root
            
       
        return recursive(nums, self.root)
