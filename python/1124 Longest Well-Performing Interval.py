# Time limited

class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        n = len(hours)
        dp = [0] * n

        for i in range(n):
            tiring = 0
            non = 0

            if hours[i] > 8:
                dp[i] = 1

            for j in range(i, -1, -1):
                if hours[j] > 8:
                    tiring += 1
                else:
                    non += 1

                if non < tiring:
                    dp[i] = max(dp[i], i - j + 1)

        return max(dp)


# credit to: https://leetcode.com/problems/longest-well-performing-interval/discuss/334565/JavaC%2B%2BPython-O(N)-Solution-Life-needs-996-and-669

class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        seen = {}
        score = 0
        n = len(hours)
        res = 0
        for i in range(n):
            if hours[i] > 8:
                score += 1
            else:
                score -= 1
            if score > 0:
                res = i + 1
            seen.setdefault(score, i)
            
            if score - 1 in seen:
                res = max(res, i - seen[score - 1])
        return res
                
        
