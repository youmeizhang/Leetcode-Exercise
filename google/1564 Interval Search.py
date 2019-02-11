class Solution:
    """
    @param intervalList: 
    @param number: 
    @return: return True or False
    """
    def isInterval(self, intervalList, number):
        # Write your code here
        for interval in intervalList:
            if interval[0] <= number and interval[1] >= number:
                return "True"
        return "False"
