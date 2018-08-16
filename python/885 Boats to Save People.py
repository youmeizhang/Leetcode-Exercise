class Solution:
    def numRescueBoats(self, people, limit):
        people = sorted(people)
        n = len(people)
        l = 0
        r = n - 1
        ans = 0
        while(l <= r):
            if people[r] >= limit:
                ans += 1
                r -= 1
            elif people[r] + people[l] <= limit:
                ans += 1
                r -= 1
                l += 1
            else:
                ans += 1
                r -= 1
        return ans 
