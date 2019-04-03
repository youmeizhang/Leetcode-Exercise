class Solution(object):
    def findDisappearedNumbers(self, nums):
        if nums == []:
            return []
        return list(set(range(1, len(nums) + 1)).difference(set(nums)))
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
