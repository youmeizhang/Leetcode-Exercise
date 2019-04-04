class Solution(object):
    def largestRectangleArea(self, heights):
        stack = []
        area = 0
        top = -1
        n = len(heights)
        i = 0
        while i < n:
            if stack and heights[i] <= heights[stack[len(stack) - 1]]: 
                top = stack.pop()
                if not stack:
                    area = max(area, heights[top] * i)
                else:
                    area = max(area, heights[top] * (i - stack[len(stack) - 1] - 1))
                i -= 1

            else:
                stack.append(i)
            i += 1

        while stack != []:
            top = stack.pop()
            if not stack:
                area = max(area, heights[top] * i)
            else:
                area = max(area, heights[top] * (i - stack[len(stack) - 1] - 1))

        return area

        """
        :type heights: List[int]
        :rtype: int
        """
        
