class Solution:
    """
    @param s: the given string
    @return: all the possible states of the string after one valid move
    """
    def generatePossibleNextMoves(self, s):
        # write your code here

        res = []
        n = len(s)
        for i in range(n-1):
            if s[i:i+2] == "++":
                res.append(s[:i] + "--" + s[i+2:])
            else:
                continue
        return res
