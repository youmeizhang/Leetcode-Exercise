class Solution(object):
    def threeSumClosest(self, nums, target):
        nums = sorted(nums)
        n = len(nums)
        res = 0
        mindiff = 100000
        for i in range(n):
            l = i + 1
            r = n - 1

            while l < r:

                tmp = nums[i] + nums[l] + nums[r]
                diff = abs(tmp - target)

                if diff < mindiff:
                    mindiff = diff
                    res = tmp

                if tmp == target:
                    return tmp
                elif tmp < target:
                    l += 1
                else:
                    r -= 1

        return res
        
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
