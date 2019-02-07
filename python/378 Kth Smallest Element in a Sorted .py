#credit to: http://bookshadow.com/weblog/2016/08/01/leetcode-kth-smallest-element-in-a-sorted-matrix/

class Solution:
    def kthSmallest(self, matrix: 'List[List[int]]', k: 'int') -> 'int':
        
        def count(matrix, num):
            i = len(matrix) - 1
            j = 0
            count = 0
            while(i >= 0 and j < len(matrix[0])):
                if matrix[i][j] <= num:
                    count += i + 1
                    j += 1
                else:
                    i -= 1
            return count
            
                        
        
        l = matrix[0][0]
        r = matrix[-1][-1]
        while (l <= r):
            x = (r + l) >> 1
            if count(matrix, x) >= k:
                r = x - 1
            else:
                l = x + 1
        return l
         
