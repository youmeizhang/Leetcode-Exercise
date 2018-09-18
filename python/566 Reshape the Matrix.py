class Solution:
    def matrixReshape(self, nums, r, c):
        res = []
        for i in nums:
            res += i
        if len(nums) * len(nums[0]) != r * c:
            return nums
        new_matrix = [[0 for x in range(c)] for y in range(r)] 
        i = 0
        j = 0
        while j+c <= len(res):
            tmp = res[j:j+c]
            new_matrix[i] = tmp
            i += 1
            j += c
        return new_matrix
