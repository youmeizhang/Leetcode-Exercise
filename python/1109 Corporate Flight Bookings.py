class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        m = len(bookings)
        res = [0] * (n+1)
        
        for i, j, v in bookings:
            res[i-1] += v
            res[j] -= v
        
        for i in range(1, n+1):
            res[i] += res[i-1]
        return res[:-1]
        
