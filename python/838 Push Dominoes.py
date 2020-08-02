# credit to: https://leetcode.com/problems/push-dominoes/discuss/132332/JavaC%2B%2BPython-Two-Pointers

class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        d = "L" + dominoes + "R"
        n = len(d)
        i = 0
        res = ""
        for j in range(1, n):
            if d[j] == ".":
                continue
            
            middle = j - i - 1
            if i:
                res += d[i]
                
            if d[i] == d[j]:
                res += d[i] * middle
            elif d[i] == "L" and d[j] == "R":
                res += "." * middle
            else:
                res += "R" * (middle / 2) + "." * (middle % 2) + "L" * (middle / 2)
            i = j
        return res
                
        
