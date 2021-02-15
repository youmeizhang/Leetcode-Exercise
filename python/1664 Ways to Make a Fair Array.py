class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        odd = [0] * n
        even = [0] * n
        
        for i in range(n):
            odd[i] += odd[i-1]
            even[i] += even[i-1]
            if i % 2 == 1:
                odd[i] += nums[i]
            else:
                even[i] += nums[i]

        res = 0
        for i in range(n):
            even_ = even[i-1] + odd[n-1] - odd[i]
            odd_ = odd[i-1] + even[n-1] - even[i]
            
            
            if odd_ == even_:
                res += 1
        return res
        
