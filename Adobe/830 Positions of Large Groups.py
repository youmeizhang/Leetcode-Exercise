class Solution(object):
    def largeGroupPositions(self, S):
        n = len(S)
        tmp = S[0]
        count = 1
        start = 0
        res = []

        for i in range(1, n):
            if S[i] == tmp:
                count += 1

            else:
                if count >= 3:
                    res.append([start, i-1])

                tmp = S[i]
                count = 1
                start = i
        if count >= 3:
            res.append([start, i])
        return res
        """
        :type S: str
        :rtype: List[List[int]]
        """
        
