import sys

sys.stdin = open('input.txt')

# 0-1 배낭 문제 해결 함수 (Dynamic Programming)
def happybox():
    # 1. 초기화: 무게가 0일 때 모든 값은 0
    for i in range(N + 1):
        r_arr[i][0] = 0  # 물건이 0개인 경우, 최대 가치 0
    for w in range(W + 1):
        r_arr[0][w] = 0  # 가방 용량이 0인 경우, 최대 가치 0

    # 2. DP를 이용하여 최적의 가치 계산
    for i in range(1, N + 1):  # i: 물건 인덱스 (1부터 N까지)
        for w in range(1, W + 1):  # w: 현재 가방의 최대 수용 가능 무게 (1부터 W까지)
            if w_arr[i] > w:
                # 현재 물건의 무게가 가방의 용량을 초과하는 경우, 이전 값 유지
                r_arr[i][w] = r_arr[i - 1][w]
            else:
                # 물건을 넣는 경우와 넣지 않는 경우 중 최댓값 선택
                r_arr[i][w] = max(
                    r_arr[i - 1][w - w_arr[i]] + v_arr[i],  # 현재 물건을 선택하는 경우
                    r_arr[i - 1][w]  # 현재 물건을 선택하지 않는 경우
                )

T = int(input())

for tc in range(1, T + 1):
    # 배낭의 용량 W, 물건 개수 N 입력
    W, N = map(int, input().split())

    # 물건의 무게와 가치 저장할 배열 초기화 (1-based index 사용)
    w_arr = [0 for _ in range(N + 1)]  # 물건의 무게 저장 배열
    v_arr = [0 for _ in range(N + 1)]  # 물건의 가치 저장 배열
    r_arr = [[0] * (W + 1) for _ in range(N + 1)]  # DP 결과 저장 배열

    # 각 물건의 무게와 가치 입력
    for i in range(1, N + 1):
        w_arr[i], v_arr[i] = map(int, input().split())

    # 배낭 문제 해결
    happybox()

    # 최적의 가치 출력
    print(f"#{tc} {r_arr[N][W]}")
