class Solution(object):
    def canPermutePalindrome(self, s):
        n = len(s)
        dic = collections.Counter(s)
        count = 0
        for k in dic:
            if dic[k] % 2 == 1:
                count += 1
            elif dic[k] % 2 == 0:
                continue
        
        if n % 2 == 1 and count == 1:
            return True
        elif n % 2 == 0 and count == 0:
            return True
        return False
        """
        :type s: str
        :rtype: bool
        """
        
