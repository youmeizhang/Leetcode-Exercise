class Solution(object):
    def decodeString(self, s):
        stack = []
        stack.append(["", 1])
        num = ""
        for i in s:
            if i.isdigit():
                num += i
            elif i == "[":
                stack.append(["", int(num)])
                num = ""
            elif i == "]":
                char, k = stack.pop()
                stack[-1][0] += char * k
            else:
                stack[-1][0] += i
        return stack[0][0]
