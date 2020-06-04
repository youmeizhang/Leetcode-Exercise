class Solution(object):
    def twoCitySchedCost(self, costs):
        costs = sorted(costs, key = lambda x : -abs(x[0]-x[1]))
        print(costs)
        left = 0
        right = 0
        total = 0
        n = len(costs)
        mid = n // 2
        for i in range(n):
            if left < mid and right < mid:
                if costs[i][1] >= costs[i][0]:
                    total += costs[i][0]
                    left += 1
                else:
                    total += costs[i][1]
                    right += 1
            else:
                break
        for j in range(i, n):
            if left < mid:
                total += costs[j][0]
            elif right < mid:
                total += costs[j][1]
        return total

class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        n = len(costs) // 2
        total = 0
        diff = []
        for i in range(2*n):
            total += costs[i][0]
            diff.append(costs[i][1] - costs[i][0])
        diff.sort()
        return total + sum(diff[0:n])

