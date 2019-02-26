class Solution(object):
    def maxProduct(self, words):
        n = len(words)
        res = 0
        
        for i in range(n):
            for j in range(i+1, n):
                tmp = set(words[i]) & set(words[j])
                if len(tmp) == 0:
                    res = max(res, len(words[i] * len(words[j])))
        return res
        """
        :type words: List[str]
        :rtype: int
        """
        
