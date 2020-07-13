# Solution 1: beat 49.22%
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        row = len(s1)
        col = len(s2)
        dp = [[0] * (col+1) for _ in range(row+1)]
        for r in range(1, row+1):
            dp[r][0] = dp[r-1][0] + ord(s1[r-1])
        for c in range(1, col+1):
            dp[0][c] = dp[0][c-1] + ord(s2[c-1])
    
        for r in range(row):
            for c in range(col):
                if s1[r] == s2[c]:
                    dp[r+1][c+1] = dp[r][c]
                else:
                    dp[r+1][c+1] = min(dp[r][c+1] + ord(s1[r]), dp[r+1][c] + ord(s2[c]))
                    
        return dp[-1][-1]

# Solution 2: beat 88.55%
class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        row = len(s1)
        col = len(s2)
        dp = [[0] * col for _ in range(row)]
        
        if s1[0] != s2[0]:
            dp[0][0] = ord(s1[0]) + ord(s2[0])
       
        for c in range(1, col):
            if s1[0] == s2[c]:
                i = 0
                flag = False
                while i < c:
                    if s2[i] == s1[0]:
                        flag = True
                        break
                    else:
                        i += 1
                if flag:
                    dp[0][c] = dp[0][c-1] + ord(s2[c])
                else:
                    dp[0][c] = dp[0][c-1] - ord(s2[c])
            else:
                dp[0][c] = dp[0][c-1] + ord(s2[c])
    
        for r in range(1, row):
            if s1[r] == s2[0]:
                i = 0
                flag = False
                while i < r:
                    if s1[i] == s2[0]:
                        flag = True
                        break
                    else:
                        i += 1
                if flag:
                    dp[r][0] = dp[r-1][0] + ord(s1[r])
                else:
                    dp[r][0] = dp[r-1][0] - ord(s1[r])
            else:
                dp[r][0] = dp[r-1][0] + ord(s1[r])

        for r in range(1, row):
            for c in range(1, col):
                if s1[r] == s2[c]:
                    dp[r][c] = dp[r-1][c-1]
                else:
                    dp[r][c] = min(dp[r-1][c] + ord(s1[r]), dp[r][c-1] + ord(s2[c]))
                    
        
        # print(dp)
        return dp[-1][-1]
                    
