import sys
from collections import deque
sys.stdin = open("sample_input.txt", "r")

tunnel_info = {
    1: [(-1,0), (1,0), (0,-1), (0,1)],  # 상하좌우
    2: [(-1,0), (1,0)],                  # 상하
    3: [(0,-1), (0,1)],                  # 좌우
    4: [(-1,0), (0,1)],                  # 상우
    5: [(1,0), (0,1)],                   # 하우
    6: [(1,0), (0,-1)],                  # 하좌
    7: [(-1,0), (0,-1)]                  # 상좌
}

connect = {
    (-1,0): (1,0),   # 상 <-> 하
    (1,0): (-1,0),   # 하 <-> 상
    (0,-1): (0,1),   # 좌 <-> 우
    (0,1): (0,-1)    # 우 <-> 좌
}

def solve():
    queue = deque([(r, c, 1)])  # 시작점, 시간=1부터
    visited = [[False] * m for _ in range(n)]
    visited[r][c] = True
    count = 1  # 시작점 포함
    
    while queue:
        curr_r, curr_c, time = queue.popleft()
        
        # 시간이 l에 도달했으면 더 이상 이동하지 않음
        if time >= l:
            continue
        
        # 현재 위치의 터널 구조 확인
        if tunnel_map[curr_r][curr_c] == 0:
            continue
            
        tunnel_type = tunnel_info[tunnel_map[curr_r][curr_c]]
        
        # 4방향으로 이동 시도
        for dr, dc in tunnel_type:
            nr = curr_r + dr
            nc = curr_c + dc
            
            # 경계 체크
            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue
            
            # 이미 방문했으면 스킵
            if visited[nr][nc]:
                continue
            
            # 다음 위치에 터널이 없으면 스킵
            if tunnel_map[nr][nc] == 0:
                continue
            
            # 터널 연결성 확인: 다음 위치에서 현재 방향의 반대 방향이 있어야 함
            opposite_dir = connect[(dr, dc)]
            if opposite_dir not in tunnel_info[tunnel_map[nr][nc]]:
                continue
            
            # 방문 처리 및 큐에 추가
            visited[nr][nc] = True
            queue.append((nr, nc, time + 1))
            count += 1
    
    return count

T = int(input())
for tc in range(1, T + 1):
    n, m, r, c, l = map(int, input().split())
    tunnel_map = []
    for i in range(n):
        tunnel_map.append(list(map(int, input().split())))
    
    result = solve()
    print(f"#{tc} {result}")