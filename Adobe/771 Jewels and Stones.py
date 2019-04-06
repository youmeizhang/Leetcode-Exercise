class Solution(object):
    def numJewelsInStones(self, J, S):
        s_dic = collections.Counter(S)
        n = len(J)
        total = 0
        for i in range(n):
            total += s_dic[J[i]]
        return total
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        
