class Solution(object):
    def fourSum(self, nums, target):
        def threeSum(nums, target):
            nums = sorted(nums)
            n = len(nums)
            res = []
            for i in range(n-2):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                l = i+1
                r = n-1
                while l < r:            
                    total = nums[l] + nums[i] + nums[r]
                    if total == target:
                        res.append([nums[l], nums[i], nums[r]])
                        l += 1
                        r -= 1
                    elif total < target:
                        l += 1
                    else:
                        r -= 1
            return res

        nums = sorted(nums)
        n = len(nums)
        res = []
        for i in range(n):
            new_target = target - nums[i]
            tmp = threeSum(nums[:i] + nums[i+1:], new_target)
            #print(tmp)
            for tup in tmp:
                tmp2 = copy.deepcopy(tup)
                tmp2.append(nums[i])
                tmp2 = sorted(tmp2)
                if tmp2 in res:
                    continue
                else:
                    res.append(tmp2)
        return res

