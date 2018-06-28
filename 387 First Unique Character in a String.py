class Solution(object):
    def firstUniqChar(self, s):
        if len(s) == 0:
            return -1
        dic = {}
        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        for j in range(len(s)):
            if dic[s[j]] == 1:
                return j
        return -1
