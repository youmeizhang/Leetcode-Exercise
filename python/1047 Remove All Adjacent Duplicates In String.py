class Solution(object):
    def removeDuplicates(self, S):
        n = len(S)
        res = [S[0]]

        for i in range(1, n):
            if res and S[i] != res[-1]:
                res.append(S[i])
            elif res and S[i] == res[-1]:
                res.pop()
            elif not res:
                res.append(S[i])
            else:
                continue

        return ''.join(res)
        """
        :type S: str
        :rtype: str
        """
