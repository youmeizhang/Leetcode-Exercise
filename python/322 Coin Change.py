def coinChange(amount, coins):
    dp = [0] + [float('inf')] * amount
    for coin in coins:
        for j in range(amount+1):
            if j >= coin:
                dp[j] = min(dp[j], 1 + dp[j-coin])
    return dp[amount]
