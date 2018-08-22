class Solution:
    def constructRectangle(self, area):
        tmp = int(math.sqrt(area))
        while (area % tmp != 0):
            tmp -= 1
        ans = [int(area / tmp), tmp]
        return ans
