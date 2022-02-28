def maxScore(nums):
    nums.insert(0, 1)
    nums.append(1)
    n = len(nums)
    if n == 1:
        return nums[0]
    if n == 2:
        if nums[0] > nums[1]:
            return nums[0]*nums[1] + nums[0]
        else:
            return nums[0]*nums[1] + nums[1]

    m = [[0 for x in range(n)] for x in range(n)]

    for i in range(1, n):
        m[i][i] = 0

    for L in range(2, n):
        for i in range(1, n-L + 1):
            j = i + L - 1
            max = 0
            for k in range(i, j):
                tmp = m[i][k] + m[k + 1][j] + nums[i - 1] * nums[k] * nums[j]
                if tmp > max:
                    m[i][j] = tmp
                    max = tmp
    print(m[1][n-1])
    return m[1][n - 1]

maxScore([3,1,5,5])