class Solution:
    def findLUSlength(self, strs):
        n = len(strs)
        res = -1
        for i in range(n):
            status = False
            for j in range(n):
                if i == j:
                    continue
                elif self.isSubString(strs[i], strs[j]):
                    status = True
                    break
            if not status:
                res = max(res, len(strs[i]))
        return res

    def isSubString(self, str1, str2):
        if str1 == str2: return True
        if len(str1) > len(str2): return False
        pos = 0
        for i in range(len(str2)):
            if pos == len(str1):
                break
            if str1[pos] == str2[i]:
                pos += 1
        return pos == len(str1)
