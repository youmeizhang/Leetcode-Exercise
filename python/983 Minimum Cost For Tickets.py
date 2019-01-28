class Solution(object):
    def mincostTickets(self, days, costs):
        dp = [0] * (days[-1] + 1)
        
        for i in range(1, len(dp)):
            if i in days:
                dp[i] = min(dp[max(0, i-1)] + costs[0], dp[max(0, i-7)] + costs[1], dp[max(0, i-30)]+costs[2])
            else:
                dp[i] = dp[i-1]
            
        return dp[-1]
        
credit to: huahuajiang
