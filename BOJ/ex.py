def findTargetSumWays(nums, target):
    tot = sum(nums)
    if ((tot - target) % 2 != 0 or target > tot):
        return 0
    s1 = (tot - target) // 2
    n = len(nums)
    dp = [[0 for x in range(s1 + 1)] for y in range(n + 1)]
    dp[0][0] = 1

    # Count of subset with given sum logic
    for i in range(1, n + 1):
        for j in range(0, s1 + 1):
            if (nums[i - 1] <= j):
                dp[i][j] = dp[i - 1][j - nums[i - 1]] + dp[i - 1][j]
            elif (nums[i - 1] > j):
                dp[i][j] = dp[i - 1][j]

    return dp[n][s1]

findTargetSumWays([1,1,1,1,1],3)