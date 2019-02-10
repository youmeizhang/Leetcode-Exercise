class Solution:
    def equationsPossible(self, equations: 'List[str]') -> 'bool':
        idx = [i for i in range(26)]
        base = ord('a')
        def find(x):
            while x != idx[x]:
                x = idx[x]
            return x
        def union(i, j):
            ii, jj = find(i), find(j)
            idx[ii] = jj

        for eq in equations:
            if eq[1] == "=":
                union(ord(eq[0]) - base, ord(eq[3]) - base)

        for eq in equations:    
            if eq[1] == "!":
                if find(ord(eq[0]) - base) == find(ord(eq[3]) - base):
                    return False
        return True
