class Solution:
    """
    @param s: Roman representation
    @return: an integer
    """
    def romanToInt(self, s):
        # write your code here
        dic = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        res = dic[s[0]]
        for i in range(1, len(s)):
            if dic[s[i]] > dic[s[i-1]]:
                res -= dic[s[i-1]]
                res += dic[s[i]] - dic[s[i-1]]
            else:
                res += dic[s[i]]
        return res
