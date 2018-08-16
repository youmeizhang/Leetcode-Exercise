class Solution(object):
    def scoreOfParentheses(self, S):
        stack = 0
        score = [0 for i in range(30)]
    
        def get_score(ith):
            if score[ith + 1] == 0:
                score[ith] += 1
            else:
                score[ith] += 2 *(score[ith + 1])
                score[ith + 1] = 0
        for i in S:
            if i == "(":
                stack += 1
            else:
                get_score(stack)
                stack -= 1
        return score[1]
