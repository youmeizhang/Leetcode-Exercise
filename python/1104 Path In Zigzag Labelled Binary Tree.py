# credit to: https://www.youtube.com/watch?v=wsI_co96ltY

class Solution(object):
    def pathInZigZagTree(self, label, s = 0):
        if label == 1:
            return [1]
        parent = label / 2
        if s == 0:
            s = 1
            while s < label:
                s = s * 2 + 1
            s = s + s / 2 + 1
        
        return self.pathInZigZagTree(s / 2 - parent, s / 2) + [label]
        """
        :type label: int
        :rtype: List[int]
        """
        
