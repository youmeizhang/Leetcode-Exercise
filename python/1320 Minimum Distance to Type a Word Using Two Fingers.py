# credit to: https://www.youtube.com/watch?v=GRRDl3HxQAI&t=599s

class Solution(object):
    def minimumDistance(self, word):
        """
        :type word: str
        :rtype: int
        """
        #two fingers
        
        # dist[i][l][r]: from i to j, the minimum dist
        # dist[i][l][r] = min(dist[i+1][c][r] + cost(l, c), dist[i+1][l][c] + cost(r, c))
        
        n = len(word)
        dist = [[[0] * 27 for _ in range(27)] for _ in range(n)]
        
        def cost(a, b):
            if a == 26:
                return 0
            return abs(a // 6 - b // 6) + abs(a % 6 - b % 6)
        
        def dp(i, l, r):
            if i == n:
                return 0
            if dist[i][l][r]:
                return dist[i][l][r]
            c = ord(word[i]) - ord('A')
            dist[i][l][r] = min(dp(i+1, c, r) + cost(l, c), dp(i+1, l, c) + cost(r, c))
            return dist[i][l][r]
        
        return dp(0, 26, 26)
        
        
        
        
        
