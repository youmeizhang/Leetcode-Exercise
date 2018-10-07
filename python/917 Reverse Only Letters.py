class Solution:
    def reverseOnlyLetters(self, S):
        S_copy = S
        res = ''
        n = len(S)
        j = n-1
        for i in range(n):
            if S[i].isalpha() and S[j].isalpha():
                res += S[j]
                j -= 1
            elif S[i].isalpha():
                while(not S[j].isalpha()):
                    j -= 1
                res += S[j]
                j -= 1
            else:
                res += S[i]
        return res
