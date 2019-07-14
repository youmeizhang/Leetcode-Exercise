# Time limited

class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        n = len(hours)
        dp = [0] * n

        for i in range(n):
            tiring = 0
            non = 0

            if hours[i] > 8:
                dp[i] = 1

            for j in range(i, -1, -1):
                if hours[j] > 8:
                    tiring += 1
                else:
                    non += 1

                if non < tiring:
                    dp[i] = max(dp[i], i - j + 1)

        return max(dp)


