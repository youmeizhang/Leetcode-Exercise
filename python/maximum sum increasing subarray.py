def maxSum(nums):
    n = len(nums)
    dp = [0] * n
    idx = [0] * n
    for i in range(n):
        dp[i] = nums[i]
        idx[i] = i
    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                if dp[j] + nums[i] > dp[i]:
                    dp[i] = max(dp[i], dp[j] + nums[i])
                    idx[i] = j
    return max(dp)
