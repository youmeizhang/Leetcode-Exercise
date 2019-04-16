# credit to: https://blog.csdn.net/fuxuemingzhu/article/details/79559691

class Solution(object):
    def topKFrequent(self, words, k):
        dic = collections.Counter(words)
        candidates = dic.keys()
        candidates.sort(key = lambda w : (-dic[w], w))
        return candidates[:k]
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
           
class Solution(object):
    def topKFrequent(self, words, k):
        dic = collections.Counter(words)
        heap = [(-freq, word) for word, freq in dic.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        
