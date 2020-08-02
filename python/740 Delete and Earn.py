# credit to: https://www.youtube.com/watch?v=YzZd-bsMthk

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 1:
            return 0
        dic = collections.defaultdict(int)
        for i in range(n):
            dic[nums[i]] += nums[i]
        
        l = [0] * max(nums)
        for i, k in enumerate(dic):
            l[k-1] = dic[k]
        
        m = len(l)
        dp = [0] * (m+1)
        dp[0] = 0
        dp[1] = l[0]
        for i in range(1, m):
            dp[i+1] = max(dp[i], dp[i-1] + l[i])
        return max(dp)
            
        
