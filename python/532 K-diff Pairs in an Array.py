class Solution:
    def findPairs(self, nums, k):
        if k == 0:
            nums = [item for item, count in collections.Counter(nums).items() if count > 1]
            return len(nums)
        elif k > 0:
            return len(set(nums) & set(v+k for v in nums))
        else:
            return 0
            
#Time Limit
class Solution:
    def findPairs(self, nums, k):
        ans = 0
        if k == 0:
            new_nums = [item for item, count in collections.Counter(nums).items() if count > 1]
            return len(new_nums)

        new_nums = list(set(nums))
        n = len(new_nums)
        for i in range(0, n):
            for j in range(i+1, n):
                if abs(new_nums[i] - new_nums[j]) == k:
                    #print(i, j)
                    ans += 1
        return ans
