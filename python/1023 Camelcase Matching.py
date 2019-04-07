class Solution(object):
    def camelMatch(self, queries, pattern):
        n = len(queries)
        res = [False] * n
        for i in range(n):
            word = queries[i]
            k = 0
            for j in range(len(word)):                
                if word[j] == pattern[k]:
                    k += 1
                    if k == len(pattern):
                        if not any(x.isupper() for x in word[j+1:]):
                            res[i] = True
                            break
                        else:
                            break

                elif word[j].isupper():
                    res[i] = False
                    break
                else:
                    continue
        return res
        """
        :type queries: List[str]
        :type pattern: str
        :rtype: List[bool]
        """
        
