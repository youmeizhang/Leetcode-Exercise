class Solution(object):
    def validPalindrome(self, s):
        def valid(a):
            left = 0
            right = len(a) - 1
            while left <= right:
                if a[left] != a[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        l = 0
        r = len(s) - 1
        while l <= r:
            if s[l] != s[r]:
                tmp_left = s[:l] + s[l+1:] 
                tmp_right = s[:r] + s[r+1:]
                return valid(tmp_left) or valid(tmp_right)
                
            l += 1
            r -= 1
        return True
            
        """
        :type s: str
        :rtype: bool
        """
        
