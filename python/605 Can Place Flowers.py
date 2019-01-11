class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        if flowerbed == [0] and n < 2:
            return True
        if flowerbed == [0, 0] and n < 2:
            return True
        i = 1
        while n > 0 and i < len(flowerbed) - 1:
            if i == 1 and flowerbed[i - 1] == 0 and flowerbed[i] == 0:
                i += 1
                n -= 1
            elif flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i + 1] == 0:
                n -= 1
                i += 2
            else:
                i += 1
        if n != 0 and i == len(flowerbed) - 1 and flowerbed[i - 1] == 0 and flowerbed[i] == 0:
            n -= 1
            
        if n == 0:
            return True
        else:
            return False
