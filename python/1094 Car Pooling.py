# credit to: https://leetcode.com/problems/car-pooling/discuss/317712/Simple-Python-solution-(Meeting-Rooms-II)

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        l = []
        for n, start, end in trips:
            l.append((start, n))
            l.append((end, -1*n))
        l.sort()
        
        cnt = 0
        for tup in l:
            cnt += tup[1]       
            if cnt > capacity:
                return False
        return True
