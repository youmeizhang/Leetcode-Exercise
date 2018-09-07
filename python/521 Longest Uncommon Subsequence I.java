class Solution:
    def findLUSlength(self, a, b):
        return max(len(a), len(b)) if a != b else -1
