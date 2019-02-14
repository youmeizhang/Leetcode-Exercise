class Solution:
    def shortestPalindrome(self, s: 'str') -> 'str':
        rev_s = s[::-1]
        
        l = s + "#" + rev_s
        p = [0] * len(l)
        for i in range(1, len(l)):
            j = p[i-1]
            while(j > 0 and l[i] != l[j]):
                j = p[j-1]
            if l[i] == l[j]:
                p[i] = j + 1
        return rev_s[ : len(s) - p[len(l) - 1]] + s
