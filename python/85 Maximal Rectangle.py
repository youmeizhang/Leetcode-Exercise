class Solution(object):
    def maximalRectangle(self, matrix):
        def largestRectangleArea(heights):
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

        row = len(matrix)
        if row == 0:
            return 0

        column = len(matrix[0])

        dp = []
        for i in range(column):
            if matrix[0][i] == "1":
                dp.append(1)
            else:
                dp.append(0)

        if row == 1:
            return largestRectangleArea(dp)

        res = largestRectangleArea(dp)
        
        for i in range(1, row):
            for j in range(column):
                if matrix[i][j] == "1":
                    dp[j] = dp[j] + int(matrix[i][j])
                else:
                    dp[j] = 0

            tmp = largestRectangleArea(dp)
            res = max(res, tmp)

        return res
