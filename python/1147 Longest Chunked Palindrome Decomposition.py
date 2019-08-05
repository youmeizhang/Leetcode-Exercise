# credit to: https://leetcode.com/problems/longest-chunked-palindrome-decomposition/discuss/350560/JavaC%2B%2BPython-Easy-Greedy-with-Prove

class Solution:
    def longestDecomposition(self, text: str) -> int:
        res = 0
        l = ""
        r = ""
        for i, j in zip(text, text[::-1]):
            l, r = l + i, j + r
            if l == r:
                res += 1
                l = ""
                r = ""
        return res
        
