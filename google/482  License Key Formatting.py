class Solution:
    def licenseKeyFormatting(self, S: 'str', K: 'int') -> 'str':
        S = S.replace("-", "")
        i = len(S) - 1
        res = ""
        while (i - K >= 0):
            res = S[i - K + 1:i+1] + "-" + res
            i = i - K
        res = S[0:i+1] + "-" + res
        return res[:-1].upper()
