class Solution:
    def racecar(self, target: int) -> int:
        m_ = [0] * (target + 1)
        
        def dp(t):
            if m_[t] > 0:
                return m_[t]
            n = math.ceil(math.log(t+1, 2))
            if 2**n == t + 1:
                m_[t] = n
                return n
            
            m_[t] = n + 1 + dp(2**n - 1 - t)
            for m in range(n-1):
                curr = 2**(n-1) - 2**m
                m_[t] = min(m_[t], n + m + 1 + dp(t - curr))
            return m_[t]
    
        return dp(target)

        
