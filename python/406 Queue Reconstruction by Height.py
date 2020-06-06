class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        height = []
        dic = collections.defaultdict(list)
        for person in people:
            if person[0] not in height:
                height.append(person[0])
            dic[person[0]].append(person)
        
        height.sort()

        res = []
        while height:
            h = height.pop()

            tmp = dic[h]
            tmp.sort(key=lambda x : x[1])
            for t in tmp:
                res.insert(t[1], t)
        return res
            
        
