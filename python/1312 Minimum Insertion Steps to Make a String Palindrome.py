from functools import lru_cache
class Solution(object):
    def minInsertions(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        @lru_cache(None)
        def dp(i, j):
            if i >= j:
                return 0
            return dp(i+1,j-1) if s[i] == s[j] else min(dp(i+1,j) + 1, dp(i,j-1)+1)
        return dp(0, len(s)-1)
        
