class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        min_x = min(rec1[0], rec1[2])
        max_x = max(rec1[0], rec1[2])

        min_y = min(rec1[1], rec1[3])
        max_y = max(rec1[1], rec1[3])

        min2_x = min(rec2[0], rec2[2])
        max2_x = max(rec2[0], rec2[2])

        min2_y = min(rec2[1], rec2[3])
        max2_y = max(rec2[1], rec2[3])

        if min2_x > min_x and min2_x < max_x:
            if min2_y >= max_y or max2_y <= min_y:
                return False
            else:
                return True

        if max2_x < max_x and max2_x > min_x:
            if min2_y >= max_y or max2_y <= min_y:
                return False
            else:
                return True
        
        if max_x <= max2_x and min_x >= min2_x:
            if max_y <= min2_y or min_y >= max2_y:
                return False
            else:
                return True

        return False
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        
