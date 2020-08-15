class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n = len(arr)
        dic = collections.defaultdict(int)
        res = 1
        for num in arr:
            first = num - difference
            if first in dic:
                res = max(res, dic[first] + 1)
                dic[num] = dic[first] + 1
            else:
                dic[num] = 1
        return res
                
