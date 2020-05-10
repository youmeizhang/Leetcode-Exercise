class Solution(object):
    def findJudge(self, N, trust):
        if trust == []:
            return 1
        
        dic = collections.defaultdict(int)

        for pair in trust:
            dic[pair[1]] += 1

        res = -1
        max_value = max(dic.values())

        for i, key in enumerate(dic):
            if dic[key] == max_value:
                if res != -1:
                    return -1
                else:
                    res = key
          
        for pair in trust:
            if pair[0] == res:
                return -1
        return res
        
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        
# credit to: https://leetcode.com/explore/featured/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3325/discuss/242938/JavaC++Python-Directed-Graph        
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        count = [0] * (N+1)
        for i, j in trust:
            count[i] -= 1
            count[j] += 1
            
        for i in range(1, N+1):
            if count[i] == N-1:
                return i
        return -1
