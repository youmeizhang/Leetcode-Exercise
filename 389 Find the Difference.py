class Solution(object):
    def findTheDifference(self, s, t):
        dic = {}
        for i in range(len(s)):
            if s[i] in dic:
                dic[s[i]] += 1
            else:
                dic[s[i]] = 1

        for i in range(len(t)):
            if t[i] in s:
                dic[t[i]] -= 1
            else:
                return t[i]

        for key, value in dic.items():
            if value != 0:
                return key
