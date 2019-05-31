class Solution(object):
    def validPalindrome(self, s):
        if s == s[::-1]:
            return True
        def valid(s):
            return s == s[::-1]
        n = len(s)
        l = 0
        r = n - 1
        while l <= r:
            if s[l] != s[r]:
                if valid(s[:l] + s[l+1:]) or valid(s[:r] + s[r+1:]):
                    return True
                else:
                    return False
            l += 1
            r -= 1
        return False
                
        """
        :type s: str
        :rtype: bool
        """
        
