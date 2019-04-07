# credit to: https://leetcode.com/problems/video-stitching/discuss/270036/Python-Greedy-Solution-O(1)-Space

class Solution(object):
    def videoStitching(self, clips, T):
        end, end2, res = -1, 0, 0
        
        for i, j in sorted(clips):
            if end2 >= T or i > end2:
                break
            elif end < i <= end2:
                res, end = res + 1, end2
            end2 = max(end2, j)
            
        return res if end2 >= T else -1
        """
        :type clips: List[List[int]]
        :type T: int
        :rtype: int
        """
