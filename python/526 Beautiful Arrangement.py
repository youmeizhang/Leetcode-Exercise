class Solution:
    def countArrangement(self, N):
        dic = {}

        def helper(idx, nums):
            if not nums: return 1
            key = idx, tuple(nums)

            if key in dic: return dic[key]
            ans = 0
            for i, n in enumerate(nums):
                if n % idx == 0 or idx % n == 0:
                    ans += helper(idx + 1, list(nums[:i]) + list(nums[i+1:]))
            dic[key] = ans
            return ans
        return helper(1, range(1, N+1))
