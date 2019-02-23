class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        res = list(itertools.product(nums1, nums2))
        return sorted(res, key = lambda x : sum(x))[:k]
    
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        
# credit to: http://bookshadow.com/weblog/2016/07/07/leetcode-find-k-pairs-with-smallest-sums/

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        n1 = len(nums1)
        n2 = len(nums2)
        j = 0
        res = []
        heap = [(float('inf'), None, None)]
        while len(res) < min(k, n1 * n2):
            if j < n2:
                total, p, q = heap[0]
                if nums1[0] + nums2[j] < total:
                    for i in range(n1):
                        heapq.heappush(heap, (nums1[i] + nums2[j], i, j))
                    j += 1
            total, p, q = heapq.heappop(heap)
            res.append([nums1[p], nums2[q]])
        return res

        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        
