# credit to: http://zxi.mytechroad.com/blog/dynamic-programming/688-knight-probability-in-chessboard/
class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        dp0 = [[0] * N for _ in range(N)]
        dp0[r][c] = 1
        for k in range(1, K+1):
            dp1 = [[0] * N for _ in range(N)]
            for i in range(N):
                for j in range(N):
                    sum_ = 0
                    for di, dj in zip([-2,-1,1,2,2,1,-1,-2], [-1,-2,-2,-1,1,2,2,1]):
                        new_i = di + i
                        new_j = dj + j
                        if new_i in range(N) and new_j in range(N):
                            dp1[i][j] += dp0[new_j][new_i]
            dp1, dp0 = dp0, dp1

        total = 0
        for i in range(N):
            for j in range(N):
                total += dp0[i][j]
        return total / 8 ** K
                    
