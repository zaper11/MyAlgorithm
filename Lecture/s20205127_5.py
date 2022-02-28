def search(heights):
    m, n = len(heights), len(heights[0])
    chi = [[-1 for _ in range(n)] for _ in range(m)]
    jap = [[-1 for _ in range(n)] for _ in range(m)]

    def dfs(dp, i, j, flag, seen):
        if (0 <= i < m and 0 <= j < n) and (i, j) not in seen:
            if flag == 1 and (i == 0 or j == 0):
                dp[i][j] = "C"
                return 1

            if flag == 0 and (i == m - 1 or j == n - 1):
                dp[i][j] = "J"
                return 1

            if dp[i][j] == "C" or dp[i][j] == "J":
                return 1

            seen.add((i, j))
            if (0 <= i+1 < m and 0 <= j < n) and heights[i + 1][j] <= heights[i][j] and dfs(dp, i + 1, j, flag, seen):
                dp[i][j] = "C" if flag == 1 else "J"

            if (0 <= i-1 < m and 0 <= j < n) and heights[i - 1][j] <= heights[i][j] and dfs(dp, i - 1, j, flag, seen):
                dp[i][j] = "C" if flag == 1 else "J"

            if (0 <= i < m and 0 <= j+1 < n) and heights[i][j + 1] <= heights[i][j] and dfs(dp, i, j + 1, flag, seen):
                dp[i][j] = "C" if flag == 1 else "J"

            if (0 <= i < m and 0 <= j-1 < n) and heights[i][j - 1] <= heights[i][j] and dfs(dp, i, j - 1, flag, seen):
                dp[i][j] = "C" if flag == 1 else "J"
            seen.remove((i, j))

            if dp[i][j] == "C" or dp[i][j] == "J":
                return 1

        return 0

    res = []
    for i in range(m):
        for j in range(n):
            if chi[i][j] != "C":
                dfs(chi, i, j, 1, set())
            if jap[i][j] != "J":
                dfs(jap, i, j, 0, set())

            if chi[i][j] == "C" and jap[i][j] == "J":
                res.append([i, j])
    return res
