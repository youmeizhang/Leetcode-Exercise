class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        def dfs(idx, fuel):
            res = 0
            if idx == finish:
                res += 1
            
            if dp[idx][fuel] != -1:
                return dp[idx][fuel]
            
            n = len(locations)
            for i in range(n):
                left_fuel = fuel - abs(locations[i] - locations[idx])
                if i != idx and left_fuel >= 0:
                    res += dfs(i, left_fuel)
                    res %= 1000000007
            
            dp[idx][fuel] = res
            return res
            
        dp = [[-1] * (fuel+1) for _ in range(len(locations)+1)]
        return dfs(start, fuel)

