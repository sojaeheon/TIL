import sys
sys.stdin = open('algo2_sample_in.txt')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def search():
    queue = []

    for x in range(M):
        for y in range(N):
            if data[x][y] != '.':
                queue.append((data[x][y], x, y, 0))

    # 알파벳 순 정렬
    queue = sorted(queue)

    # 알파벳별 최대 성장 가능 크기 딕셔너리
    growth_tracker = {chr(65 + i): max_growth[i] for i in range(len(max_growth))}
    while queue:
        bacteria, x, y, current_growth = queue.pop(0)

        # 최대 성장 가능치에 도달했으면 종료.
        if current_growth >= growth_tracker[bacteria]:
            continue

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < M and 0 <= ny < N and data[nx][ny] == '.':
                data[nx][ny] = bacteria
                queue.append((bacteria, nx, ny, current_growth + 1))


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    num = int(input())
    max_growth = list(map(int, input().split()))
    data = [input().split() for _ in range(M)]

    search()
    print(f'#{tc}')
    for f in data:
        print(*f)

