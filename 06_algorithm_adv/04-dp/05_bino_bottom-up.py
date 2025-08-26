def bino(n, k):
    dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
    '''
        [0, 0, 0, 0]
        [0, 0, 0, 0]
        [0, 0, 0, 0]
        [0, 0, 0, 0]
    '''
    for i in range(n+1):
        for j in range(min(i, k) + 1):
            if j == 0 or i == j:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
    '''
        [1, 0, 0, 0, 0]
        [1, 1, 0, 0, 0]
        [1, 2, 1, 0, 0]
        [1, 3, 3, 1, 0]
        [1, 4, 6, 4, 1]
    '''
    return dp[n][k]


n = 100000
k = 100000
print(bino(n, k))  # 출력: 10
