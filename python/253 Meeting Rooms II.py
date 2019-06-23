class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        l = []
        for start, end in intervals:
            l.append((start, 1))
            l.append((end, -1))
        l.sort()
        
        cnt = 0
        res = 0
        for tup in l:
            cnt += tup[1]
            res = max(res, cnt)
        return res
