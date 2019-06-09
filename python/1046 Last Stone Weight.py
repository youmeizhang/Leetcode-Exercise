class Solution(object):
    def lastStoneWeight(self, stones):
        for i in range(len(stones)):
            stones[i] *= -1

        heapq.heapify(stones)
        while len(stones) > 1:
            max_1 = heapq.heappop(stones)
            max_2 = heapq.heappop(stones)
            tmp = -1 * max_1 - -1 * max_2
            heapq.heappush(stones, -1 * tmp)

        return -1 * stones[0] if stones else 0
        """
        :type stones: List[int]
        :rtype: int
        """
