class Solution:
    """
    @param target: the target string
    @param s: 
    @return: output all strings containing target  in s
    """
    def getAns(self, target, s):
        # Write your code here
        def compare(target, word):
            if len(word) < len(target):
                return False
            i = 0
            n = len(target) - 1
            j = 0
            m = len(word) - 1
            while(i <= n and j <= m):
                if target[i] == word[j] and i == n:
                    return True
                elif target[i] == word[j]:
                    i += 1
                    j += 1
                else:
                    j += 1
            return False
            
        res = []
        for word in s:
            if compare(target, word):
                res.append(word)
        return res
