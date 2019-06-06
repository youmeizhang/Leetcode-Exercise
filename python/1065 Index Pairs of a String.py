class Solution(object):
    def indexPairs(self, text, words):
        res = []
        m = len(text)
        for word in words:
            n = len(word)
            for i in range(m - n + 1):
                if text[i:i+n] == word:
                    res.append([i,i+n-1])

        res.sort(key = lambda x : [x[0],x[1]])

        return res
        """
        :type text: str
        :type words: List[str]
        :rtype: List[List[int]]
        """
