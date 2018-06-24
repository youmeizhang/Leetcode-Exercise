class Solution(object):
    def buddyStrings(self, A, B):
        lenA, lenB = len(A), len(B)
        if lenA == lenB == 0:
            return False
        if lenA != lenB:
            return False
        res = [i for i in range(len(A)) if A[i] != B[i]]
        if len(res) == 0 and self.isPalindrome(A):
            return True
        elif len(res) == 0 and A[:int(lenA/2)] == A[int(lenA/2):]:
            return True
        elif len(res) != 2:
            return False
        elif A[res[0]] == B[res[1]] and A[res[1]] == B[res[0]]:
            return True
        else:
            return False
    
    def isPalindrome(self, a):
        result = [i for i in a.lower() if i.isalnum()]
        if result == result[::-1]:
            return True
        else:
            return False
