import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    # 1부터 N까지의 정수 배열
    nums = list(range(1, N+1))
    result = 0  # 부분집합의 원소의 합이 K가 되는 경우가 있으면 1씩 증가

    # 값들을 기록 (현재까지 고려한 숫자들로 s를 만드는 부분집합의 개수)
    # dp[index] 번째에 기록할 값은
        # 각 요소들의 합이 index가 되는 경우 + 1
    #       0  1  2  3  4  5  6  ...
    # dp = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, .... ]
    dp = [0] * (K + 1)      # 목표값이 K 이므로 K까지만 고려
    dp[0] = 1       # 합이 0이되는 경우는 공집합 1개

    # 상향식 조사
    for num in range(1, N + 1): # 공집합은 필요없음.
        # num을 사용한다.
        # 단, s >= num인 부분만 업데이트
            # 우리의 최종 목표 K번째에 누적해 나갈 것
            # 내 현재 num보다 작은 경우를 num으로 더해서 만들 수는 없음!
        for s in range(K, num - 1 , -1):
            dp[s] += dp[s-num]
    print(dp)
    print(dp[K])


