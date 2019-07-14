class Solution:
    def groupAnagrams(self, strs):
        dic = {}
        res = []
        count = 0
        for i in range(len(strs)):
            word = ''.join(sorted(strs[i]))
            
            if word in dic:
                res[dic[word]].append(strs[i])
            else:
                res.append([strs[i]])
                dic[word] = count
                count += 1
        return res
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
