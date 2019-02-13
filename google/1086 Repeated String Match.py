class Solution:
    """
    @param A: a string
    @param B: a string
    @return: return an integer
    """
    def repeatedStringMatch(self, A, B):
        # write your code here
        count = 1
        if B in A:
            return count
        orig = ""
        for i in A:
            orig += i
        while(count < len(B)):
            A = A + orig
            count += 1
            if B in A:
                return count
            else:
                continue
        return -1
