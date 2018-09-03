class Solution:
    def reverseStr(self, s, k):
        n = len(s)
        res = ""
        i = 0
        while(i < n):
            res = res + s[i:i+k][::-1]
            res = res + s[i+k:i+(k*2)]
            i = i + k * 2
        return res
