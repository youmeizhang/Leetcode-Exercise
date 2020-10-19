# credit to: http://zxi.mytechroad.com/blog/searching/leetcode-464-can-i-win/

class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        M = maxChoosableInteger
        T = desiredTotal
        
        def win(M, T, m, state):
            if T <= 0:
                return False
            if m[state] != 0:
                return m[state] == 1
            for i in range(M):
                if state & (1 << i) > 0:
                    continue
                if not win(M, T - i - 1, m, state | (1 << i)):
                    m[state] = 1
                    return True
            m[state] = -1
            return False
        
        s = M * (M + 1) / 2
        if s < T:
            return False
        if T <= 0:
            return True
        if s == T:
            return (M % 2) == 1
        
        m = [0] * (1 << M)
        return win(M, T, m, 0)

        
