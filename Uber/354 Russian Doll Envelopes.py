# Time Limit
class Solution(object):
    def maxEnvelopes(self, envelopes):
        envelopes = sorted(envelopes, key=lambda x : x[0])
        n = len(envelopes)
        if n < 1:
            return 0
        dp = [1] * n

        for i in range(n):
            for j in range(i):
                if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]:

                    dp[i] = max(dp[i], dp[j] + 1)


        return max(dp)
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        
        
