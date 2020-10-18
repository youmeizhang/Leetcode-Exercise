class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [[0 for _ in range(4)] for _ in range(n)]
        
        def solve(s, M):
            if M > 3:
                return 0
            if s >= n:
                return 0
            if dp[s][M]:
                return dp[s][M]
            
            curr = 0
            best = float('-inf')
            for x in range(1, M+1):
                if s+x-1 < n:
                    curr += stoneValue[s+x-1]
                    best = max(best, curr - solve(s+x, M))
            dp[s][M] = best
            return dp[s][M]
        
        alice_score = (sum(stoneValue) + solve(0, 3)) / 2
        average = sum(stoneValue) / 2
        
        if alice_score > average:
            return 'Alice'
        elif alice_score == average:
            return 'Tie'
        else:
            return 'Bob'
    
    
                
        
