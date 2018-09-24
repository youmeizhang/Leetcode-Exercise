class Solution:
    def distributeCandies(self, candies):
        return min(len(candies) // 2, len(set(candies)))
