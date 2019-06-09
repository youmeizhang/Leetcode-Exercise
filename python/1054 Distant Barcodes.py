# credit to: https://blog.csdn.net/qq_32424059/article/details/90577822

class Solution(object):
    def rearrangeBarcodes(self, barcodes):
        dic = collections.Counter(barcodes)
    
        queue = []
        for i, key in enumerate(dic):
            queue.append([-dic[key], key])

        heapq.heapify(queue)
        pre = None
        res = []
        while queue or pre:
            if queue:
                curr = heapq.heappop(queue)
                res.append(curr[1])
                curr[0] += 1
                if curr[0] == 0:
                    curr = None
            else:
                curr = None
            if pre:
                heapq.heappush(queue, pre)
            pre = curr
        return res
        """
        :type barcodes: List[int]
        :rtype: List[int]
        """
        
