import sys
sys.stdin = open('input.txt')


def lis_length(sequence):
    n = len(sequence)
    dp = [1] * n  # 각 요소에서 끝나는 LIS의 길이

    for i in range(1, n):
        for j in range(i):
            if sequence[i] > sequence[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


T = int(input().strip())
for tc in range(1, T + 1):
    N = int(input().strip())
    sequence = list(map(int, input().strip().split()))
    
    # 결과 계산
    result = lis_length(sequence)
    
    # 결과 출력
    print(f"#{tc} {result}")
