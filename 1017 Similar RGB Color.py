class Solution:
    """
    @param color: the given color
    @return: a 7 character color that is most similar to the given color
    """
    def similarRGB(self, color):
        # Write your code here
        # 11, 22 ... they all can be divided by 17
        
        hexi = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', "a", "b", "c", "d", "e", "f"]
        
        first = color[1:3]
        second = color[3:5]
        third = color[5:7]
        
        first_res = hexi[int("0x" + first, 16) // 17] + hexi[int("0x" + first, 16) // 17]
        second_res = hexi[int("0x" + second, 16) // 17] + hexi[int("0x" + second, 16) // 17]
        third_res = hexi[int("0x" + third, 16) // 17] + hexi[int("0x" + third, 16) // 17]
        
        return "#" + first_res + second_res + third_res
