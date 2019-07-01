class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res = [0] * num_people
        i = 0
        can = 1
        while candies > 0:
            if candies >= can:
                res[i] += can
                candies -= can
                i += 1
                can += 1
                if i == num_people:
                    i = 0
            else:
                res[i] += candies
                break
        return res
            
        
