class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def lastPosition(self, nums, target):
        # write your code here
        l = 0 
        r = len(nums) - 1
        while (l <= r):
            mid = (l + r) // 2
            if nums[mid] == target:
                if mid == len(nums) - 1:
                    return mid
                elif nums[mid+1] != target:
                    return mid
                else:
                    l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1
