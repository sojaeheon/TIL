import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    # DP 배열 생성 (인덱스 1부터 N까지 사용)
    arr = [-1] * (N + 1)

    # N에 따라 초기값 설정
    for i in range(1, N + 1):
        if i == 1:
            arr[i] = 1  # 2×1 공간을 채우는 방법 1가지
        elif i == 2:
            arr[i] = 3  # 2×2 공간을 채우는 방법 3가지 (세로 2개, 가로 2개, 정사각형 1개)
        elif i == 3:
            arr[i] = 6  # 2×3 공간을 채우는 방법 6가지
        else:
            # 점화식: F(n) = F(n-1) + 2*F(n-2) + F(n-3)
            # 1. 2×1을 세로로 배치 -> 남은 공간: (n-1)
            # 2. 2×2를 배치하는 방법 2가지 -> 남은 공간: (n-2) * 2
            # 3. 2×3을 배치 -> 남은 공간: (n-3)
            arr[i] = arr[i - 1] + 2 * arr[i - 2] + arr[i - 3]

    # 최종 결과 출력
    print(f"#{tc} {arr[N]}")
