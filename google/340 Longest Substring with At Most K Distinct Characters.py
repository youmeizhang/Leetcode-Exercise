class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: 'str', k: 'int') -> 'int':
        dic = {}
        min_idx = 0
        res = 0
        for i, c in enumerate(s):
            dic[c] = i
            if len(dic) > k:
                min_idx = min(dic.values())
                del dic[s[min_idx]]
                min_idx += 1
            res = max(res, i - min_idx + 1)
        return res
