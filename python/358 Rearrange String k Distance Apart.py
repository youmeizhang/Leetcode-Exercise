class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k == 0:
            return s
        dic = collections.Counter(s)
        tmp = []
        n = len(s)
        for i, v in enumerate(dic):
            tmp.append((-1 * dic[v], v))

        heapq.heapify(tmp)
        
        res = ""
        print(tmp)
        while tmp:
            cnt = min(n, k)
            used = []
            for i in range(cnt):
                if not tmp:
                    return ""
                count, word = heapq.heappop(tmp)
                res += str(word)
                if -1 * count > 1:
                    used.append((count+1, word))
                n -= 1
            for use in used:
                heapq.heappush(tmp, use)
            
        return res
