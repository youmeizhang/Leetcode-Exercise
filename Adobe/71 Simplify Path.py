class Solution(object):
    def simplifyPath(self, path):
        stack = []
        new_path = path.split('/')
        i = 0
        while i < len(new_path):
            if new_path[i] == '..':
                if stack:
                    stack.pop()
                i = i + 1
            elif new_path[i] == '.':
                i = i + 1
            elif new_path[i] == '':
                i = i + 1
            else:
                stack.append(new_path[i])
                i = i + 1

        res = '/'.join(stack)
        return '/' + res
        """
        :type path: str
        :rtype: str
        """
        
