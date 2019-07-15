class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        new_nums = sorted(nums)
        small = new_nums[: math.ceil(n / 2)]
        big = new_nums[math.ceil(n / 2) : ]
        
        cnt = 0
        p = 0
        q = 0
        
        for i in range(n):
            if cnt % 2 == 0:
                nums[i] = small[p]
                p += 1
            else:
                nums[i] = big[q]
                q += 1
            cnt += 1
            
        #return nums
