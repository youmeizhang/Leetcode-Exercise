class Solution:
    def reverseWords(self, s):
        if len(s) == 0: return s
        s_list = s.split(" ")
        res = ''
        n = len(s_list)
        for i in range(n):
            tmp = ''.join(reversed(s_list[i]))
            res += tmp
            if i != n-1: 
                res += ' '
        return res
