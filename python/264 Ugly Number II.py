class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        i2 = 0
        i3 = 0
        i5 = 0
        nums = []
        nums.append(1)
        
        for i in range(n-1):
            new_num = min(nums[i2] * 2, nums[i3] * 3, nums[i5] * 5)
            if new_num == nums[i2] * 2:
                i2 += 1
            if new_num == nums[i3] * 3:
                i3 += 1
            if new_num == nums[i5] * 5:
                i5 += 1
            nums.append(new_num)

        return nums[-1]
            
        
