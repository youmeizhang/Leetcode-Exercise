# credit to: https://www.youtube.com/watch?v=gxYV8eZY0eQ

class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        ops = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y
        }
        
        def ways(s):
            ans = []
            n = len(s)
            for i in range(n):
                if s[i] in "+-*":
                    ans += [ops[s[i]](l, r) for l, r in itertools.product(ways(s[0:i]), ways(s[i+1:]))]
                    
            if not ans:
                ans.append(int(s))
            return ans
    
        return ways(input)
