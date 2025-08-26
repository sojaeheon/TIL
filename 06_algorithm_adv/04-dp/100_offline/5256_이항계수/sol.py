import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    # 조합을 계산할 n, a, b 입력
    n, a, b = map(int, input().split())

    # 조합에서 사용할 작은 값 선택 (C(n, min(a, b)))
    t = min(a, b)

    # DP 테이블 초기화 (n+1) x (n+1) 크기 2차원 배열
    table = [[0] * (n + 1) for _ in range(n + 1)]

    # 파스칼의 삼각형을 활용한 조합 계산
    for i in range(n + 1):  # 행: i값 (n까지)
        for j in range(min(i, t) + 1):  # 열: j값 (최대 min(i, t))
            if j == 0 or j == i:
                table[i][j] = 1  # C(i, 0) = C(i, i) = 1
            else:
                # 점화식: C(i, j) = C(i-1, j) + C(i-1, j-1)
                table[i][j] = table[i - 1][j] + table[i - 1][j - 1]

    # 결과 출력
    print(f"#{tc} {table[n][t]}")
