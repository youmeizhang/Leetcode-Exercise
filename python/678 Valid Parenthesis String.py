# credit to: https://www.youtube.com/redirect?redir_token=XF8FbFMcqijQDMz0JG7SN98lNYl8MTU1OTQ4NTk4MkAxNTU5Mzk5NTgy&v=h9Y3i7hhCpo&q=http%3A%2F%2Fzxi.mytechroad.com%2Fblog%2Fdynamic-programming%2Fleetcode-678-valid-parenthesis-string%2F&event=video_description

class Solution(object):
    def checkValidString(self, s):
        min_op = 0
        max_op = 0
        for char in s:
            if char == "(":
                min_op += 1
            else:
                min_op -= 1
                
            
            min_op = max(0, min_op)
                
            if char != ")":
                max_op += 1
            else:
                max_op -= 1
            
            if max_op < 0:
                return False
            
        return min_op == 0
        """
        :type s: str
        :rtype: bool
        """
        
