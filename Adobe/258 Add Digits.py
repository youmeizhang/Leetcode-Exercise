class Solution(object):
    def addDigits(self, num):
        while num > 9:
            s = str(num)
            total = 0
            for i in range(len(s)):
                total += int(s[i])

            num = total

        return num
        """
        :type num: int
        :rtype: int
        """
        
