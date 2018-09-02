class Solution:
    def findLongestWord(self, s, d):
        n = len(s)

        def isValid(s, word):
            i = 0
            j = 0
            m = len(word)
            n = len(s)
            while(i < m and j < n):
                if word[i] == s[j]:
                    i += 1
                    j += 1
                else:
                    j += 1
            if i == m: return True
            return False

        ans = 0
        res = []
        for word in d:
            if isValid(s, word):
                if len(word) > ans:
                    ans = len(word)
                    res = []
                    res.append(word)
                elif len(word) == ans:
                    res.append(word)
        res = sorted(res)
        return res[0] if res else ""
