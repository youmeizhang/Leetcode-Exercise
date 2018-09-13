class Solution:
    def checkRecord(self, s):
        if len(s) == 0: return True
        A_freq = s.count('A')
        if A_freq > 1:
            return False
        L_freq = s.count('LLL')
        if L_freq > 0:
            return False
        return True
        
#Solution 2:
class Solution:
    def checkRecord(self, s):
      return s.count('A') <= 1 and 'LLL' not in s
