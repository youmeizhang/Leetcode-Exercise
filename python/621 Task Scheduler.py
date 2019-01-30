class Solution(object):
    def leastInterval(self, tasks, n):
        dic = collections.Counter(tasks)
        max_task = dic.most_common()[0][1]
        
        count = 0
        for i, key in enumerate(dic):
            if dic[key] == max_task:
                count += 1
        
        return max((max_task - 1) * (n+1) + count, len(tasks))
