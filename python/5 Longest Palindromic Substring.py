class Solution(object):
    def findPalindrome(self, s, l, r):
        n = len(s)
        while(r < n and l >= 0 and s[l] == s[r]):
            l -= 1
            r += 1

        return s[l+1:r]


    def longestPalindrome(self, s):
        n = len(s)
        res = ""
        ans = ""
        for i in range(0, n):
            tmp1 = self.findPalindrome(s, i, i)
            tmp2 = self.findPalindrome(s, i, i+1)

            #print(tmp1, tmp2)
            if len(tmp1) > len(res):
                res = tmp1
            if len(tmp2) > len(res):
                res = tmp2
        return res
