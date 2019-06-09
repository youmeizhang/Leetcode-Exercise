class Solution(object):
    def longestStrChain(self, words):
        words = sorted(words, key = lambda x: len(x))
        n = len(words)
        dp = [1] * n

        def check(str1, str2):
            if len(str1) == len(str2):
                return False

            count = 0
            i = 0 #str1 small
            j = 0 #str2 larger
            while i < len(str1) and j < len(str2):
                if str1[i] != str2[j]:
                    count += 1
                    j += 1
                else:
                    i += 1
                    j += 1
            if count == 1:
                return True
            if j == len(str2) - 1 and i == len(str1):
                return True
            return False

        for i in range(1, n):
            for j in range(i):
                if len(words[i]) == len(words[j]):
                    break
                elif len(words[i]) - 1 > len(words[j]):
                    continue   
                else:
                    if check(words[j], words[i]):
                        dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
        
# time limited
        
class Solution(object):
    def longestStrChain(self, words):
        words = sorted(words, key = lambda x: len(x))
        n = len(words)

        def check(str1, str2):
            if len(str1) == len(str2):
                return False

            count = 0
            i = 0 #str1 small
            j = 0 #str2 larger
            while i < len(str1) and j < len(str2):
                if str1[i] != str2[j]:
                    count += 1
                    j += 1
                else:
                    i += 1
                    j += 1
            if count == 1:
                return True
            if j == len(str2) - 1 and i == len(str1):
                return True
            return False



        def dfs(i):
            if not visited[i]:
                visited[i] = True
                for j in range(i+1, n):
                    if check(words[i], words[j]):
                        self.count += 1
                        self.tmp.append(words[j])
                        dfs(j)
                        if self.count > self.res:
                            self.res = max(self.res, self.count)
                            self.final = self.tmp
                            self.tmp = [words[i]]
                        self.count = 1
        self.res = 0 
        self.final = []
        for i in range(n): 
            if words[i] in self.final:
                continue
            else:
                self.count = 1
                visited = [False] * n
                self.tmp = [words[i]]
                dfs(i)
                if self.count > self.res:
                    self.res = max(self.res, self.count)
                    self.final = self.tmp
                    self.tmp = []
        return self.res
