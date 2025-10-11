T = int(input())
for tc in range(1, T+1):
    N = int(input())
    farm = [list(map(int, list(input().strip()))) for _ in range(N)]

    total = 0
    center = N // 2

    for i in range(N):
        # 좌우 인덱스 범위 조절 (다이아몬드 범위)
        if i <= center:
            start = center - i
            end = center + i
        else:
            start = i - center
            end = N - (i - center) - 1

        for j in range(start, end + 1):
            total += farm[i][j]

    print(f"#{tc} {total}")
