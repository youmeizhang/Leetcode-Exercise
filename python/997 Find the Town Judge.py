class Solution(object):
    def findJudge(self, N, trust):
        if trust == []:
            return 1
        
        dic = collections.defaultdict(int)

        for pair in trust:
            dic[pair[1]] += 1

        res = -1
        max_value = max(dic.values())

        for i, key in enumerate(dic):
            if dic[key] == max_value:
                if res != -1:
                    return -1
                else:
                    res = key
          
        for pair in trust:
            if pair[0] == res:
                return -1
        return res
        
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        
