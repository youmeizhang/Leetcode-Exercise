class Solution(object):
    def findItinerary(self, tickets):
        dic = collections.defaultdict(list)
        for ticket in tickets:
            dest = dic[ticket[0]]
            dest.append(ticket[1])
            dest = sorted(dest, reverse = True)

            dic[ticket[0]] = dest

        def dfs(dic, source, res):
            while dic[source]:
                val = dic[source].pop()
                dfs(dic, val, res)
            res.append(source)
        res = []
        dfs(dic, 'JFK', res)
        return res[::-1]
        
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        
