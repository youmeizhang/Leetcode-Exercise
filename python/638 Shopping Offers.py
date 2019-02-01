class Solution:
    def shoppingOffers(self, price, special, needs):
        def dfs(price, special, needs):
            local_min = directsum(price, needs)

            for spe in special:
                remain = [needs[i] - spe[i] for i in range(len(spe) - 1)]

                if min(remain) >= 0:
                    local_min = min(local_min, spe[-1] + dfs(price, special, remain))
            return local_min

        def directsum(price, needs):
            res = 0
            for i in range(len(needs)):
                res += needs[i] * price[i]
            return res

        return dfs(price, special, needs)
