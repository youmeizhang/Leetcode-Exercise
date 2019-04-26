class Solution(object):
    def frequencySort(self, s):
        dic = collections.Counter(s)
        tup = sorted(dic.items(), key=lambda pair: pair[1], reverse=True)
        res = ""
        for key, val in tup:
            res += key * val
        return res
            
        """
        :type s: str
        :rtype: str
        """
        
