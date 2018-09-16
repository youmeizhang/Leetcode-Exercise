class Solution:
    def totalFruit(self, tree):
        if len(tree) == 0: return 0
        n = len(tree)
        queue = collections.deque([])
        tmp_list = []
        res = 0
        tmp = 0
        for i in range(n):
            if tree[i] in queue:
                tmp += 1
                tmp_list.append(tree[i])
            else:
                queue.append(tree[i])
                tmp_list.append(tree[i])
                if len(queue) > 2:
                    if tree[i - 1] != queue[0]:
                        pop = queue.popleft()
                    else:
                        last = queue.pop()
                        pop = queue.pop()
                        queue.append(last)
                    res = max(res, len(tmp_list) - 1)
                    try:
                        tmp_list = tmp_list[len(tmp_list) - list(reversed(tmp_list)).index(pop):]
                    except:
                        continue
                    tmp = len(tmp_list)
                else:
                    tmp += 1
        return max(res, tmp)
