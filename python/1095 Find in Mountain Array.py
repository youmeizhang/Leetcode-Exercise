# credit to: https://blog.csdn.net/zjucor/article/details/93382525

# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        dic = {}
        n = mountain_arr.length()
        def get(idx):
            if idx in dic:
                return dic[idx]
            else:
                dic[idx] = mountain_arr.get(idx)
                return dic[idx]
            
            
        def helper(lo, hi):
            if lo == hi:
                tmp =  get(lo)
                if tmp == target:
                    return lo
                else:
                    return float('inf')
                
            if lo > hi:
                return float('inf')
            
            mid = (lo + hi) // 2
            mid_value = get(mid)
            mid_value2 = get(mid + 1)
            

            
            #to the left side, increaseing
            if mid_value < mid_value2:
                if mid_value == target:
                    return mid
                elif mid_value > target:
                    return helper(lo, mid-1) #how about the right side? because minimum index!!
                else:
                    return helper(mid+1, hi)
                
            #to the right side, decreasing
            else:
                if mid_value == target:
                    return min(mid, helper(lo, mid-1))
                elif mid_value > target:
                    return min(helper(mid + 1, hi), helper(lo, mid-1))
                else:
                    return helper(lo, mid-1)
                
        res = helper(0, n-1)
        return res if res != float('inf') else -1
