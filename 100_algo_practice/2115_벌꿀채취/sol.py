# n * n 개의 벌통
# 두명의 일꾼 , 꿀을 채취할 수 있는 벌통의 수 M이 주어진다
# 각각의 일꾼은 가로로 연속되도록 M개의 벌통을 선택

# 서로 다른 벌통에서 채취한 꿀이 섞이게 되면 상품 가치가 떨어지게 되므로,
# 하나의 벌통에서 채취한 꿀은 하나의 용기에 담아야한다.

# 하나의 벌통에서 꿀을 채취할 때, 일부분만 채취할 수 없고 벌통에 있는 모든 꿀을 한번에 채취해야 한다
# 두 일꾼이 채취할 수 있는 꿀의 최대 양은 C 이다

# 하나의 용기에 있는 꿀의 양이 많을수록 상품가치가 높아, 각 용기에 있는 꿀의 양의 제곱만큼의 수익
#(6*6) + (1*1) + (8*8) = 101

# 두 일꾼이 얻을 수 있는 수익의 합이 최대가 되는 경우를 찾고, 그때의 최대 수익을 출력하는 프로그램


# 하나의 벌통에서 채취할 수 있는 꿀의 양은 1 이상 9이하의 정수이다
# 하나의 벌통에서 일부분의 꿀만 채취할 수 없고, 벌통에 있는 모든 꿀을 한번에 채취해야 한다.

import sys
sys.stdin = open('sample_input.txt', 'r')


# 특정 구간에서 얻을 수 있는 최대 이익 계산
def get_max_profit(arr, start, M, C):
    vals = arr[start:start+M]
    n = len(vals)
    best = 0
    # 부분집합 확인 (M 최대 5라서 가능)
    for mask in range(1, 1 << n):
        s = 0
        profit = 0
        for i in range(n):
            if mask & (1 << i):
                s += vals[i]
                profit += vals[i] * vals[i]
        if s <= C:
            best = max(best, profit)
    return best

T = int(input())
for tc in range(1, T+1):
    N, M, C = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    # 모든 구간별 최대 이익 미리 계산
    segs = []
    for r in range(N):
        for c in range(N - M + 1):
            profit = get_max_profit(grid[r], c, M, C)
            segs.append((r, c, profit))

    ans = 0
    # 두 구간 선택
    for i in range(len(segs)):
        r1, c1, p1 = segs[i]
        for j in range(i+1, len(segs)):
            r2, c2, p2 = segs[j]
            # 같은 행이면 겹치지 않게
            if r1 == r2 and not (c1 + M <= c2 or c2 + M <= c1):
                continue
            ans = max(ans, p1 + p2)

    print(f"#{tc} {ans}")


