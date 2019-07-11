# credit to: https://leetcode.com/problems/optimal-account-balancing/discuss/326379/Easy-to-Understand-DFS-Python3-Solution.

class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        balance = collections.defaultdict(int)
        for x, y, value in transactions:
            balance[x] += value
            balance[y] -= value
            
        money = sorted([v for i, v in balance.items() if v != 0])
        if not money:
            return 0
        
        def dfs(index):
            if index >= len(money):
                return 0
            if money[index] == 0:
                return dfs(index + 1)
            res = float('inf')
            for s in range(index+1, len(money)):
                if money[s] == 0 or (s > index + 1 and money[s] == money[s-1]) or money[s] * money[index] > 0:
                    continue
                money[s] += money[index]
                res = min(res, 1 + dfs(index + 1))
                money[s] -= money[index]
            return 0 if res == float('inf') else res
        return dfs(0)
