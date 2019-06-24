# credit to: https://blog.csdn.net/zjucor/article/details/93382636

from itertools import product
class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        if len(expression) == 0:
            return ''

        st = [[]]
        cnt = start = 0

        for i, v in enumerate(expression):
            if v == '{':
                if cnt == 0:
                    start = i + 1
                cnt += 1
            elif v == '}':
                cnt -= 1
                if cnt == 0:
                    st[-1].append(self.braceExpansionII(expression[start:i]))
            elif v==',':
                if cnt==0: st.append([])
            else:
                if cnt==0: st[-1].append([v])

        res = set()
        for s in st:
            tmp = product(*s)
            tmp = map(''.join, tmp)
            res = res|set(tmp)
        return sorted(res)


        
