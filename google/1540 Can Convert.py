class Solution:
    """
    @param s: string S
    @param t: string T
    @return: whether S can convert to T
    """
    def canConvert(self, s, t):
        # Write your code here
        # S = "lintcode" and T = "lint"
        i = 0
        lent = len(t) - 1
        j = 0
        lens = len(s) - 1
        while(i <= lent and j <= lens):
            if t[i] == s[j] and i == lent:
                return True
            elif t[i] == s[j]:
                i += 1
                j += 1
            else:
                j += 1
        return False
