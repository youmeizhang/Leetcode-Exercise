# credit to: https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/536/week-3-may-15th-may-21st/3330/discuss/178422/One-Pass

class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        total, maxSum, curMax, minSum, curMin = 0, A[0], 0, A[0], 0
        for a in A:
            curMax = max(curMax + a, a)
            maxSum = max(maxSum, curMax)
            curMin = min(curMin + a, a)
            minSum = min(minSum, curMin)
            total += a
            

        if maxSum <= 0:
            return maxSum
        else:
            return max(maxSum, total - minSum)
            
        



