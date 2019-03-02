class Solution(object):
    def minWindow(self, S, T):
        len_s = len(S)
        len_t = len(T)
        res = ""

        dp = [[-1] * (len_t + 1) for _ in range(len_s + 1)]
        dp[0][0] = 0

        for j in range(1, len_t + 1):
            dp[0][j] = -1

        for i in range(1, len_s + 1):
            dp[i][0] = i

        for i in range(1, len_s + 1):
            for j in range(1, len_t + 1):
                if j <= i:
                    if S[i-1] == T[j-1]:
                        dp[i][j] = dp[i-1][j-1]
                    elif S[i-1] != T[j-1]:
                        dp[i][j] = dp[i-1][j]
                else:
                    continue

            if dp[i][-1] != -1:
                if len(res) > i - dp[i][-1]:
                    res = S[dp[i][-1] : i]
                elif res == "":
                    res = S[dp[i][-1] : i]    
                else:
                    continue

        return res
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        
