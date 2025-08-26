def fibo(N):
    if N <= 1:
        return N

    # 함수 내에서 저장할 공간을 생성
    dp = [0] * (N+1)
    dp[1] = 1

    for i in range(2, N+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[N]

result = fibo(10001)
print(result)