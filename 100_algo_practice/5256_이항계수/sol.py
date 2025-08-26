
def calculate(n):
    dp = [[1]]

    for i in range(1,n+1):
        lst = []
        for j in range(0,i+1):
            if j == 0 or j == i:
                lst.append(1)
            else:
                if i == n and j == b:
                    return dp[i-1][j-1]+dp[i-1][j]
                lst.append(dp[i-1][j-1]+dp[i-1][j])
        dp.append(lst)

T = int(input())

for tc in range(1,T+1):
    n, a, b = map(int,input().split())

    result = calculate(n)
    
    print(f'#{tc} {result}')
    
    
    
