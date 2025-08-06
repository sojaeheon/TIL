import sys
sys.stdin = open("input.txt", "r")
from collections import deque

d_col = [1,-1,0,0]
d_row = [0,0,-1,1]

def search_goal(row,col):
    que = deque()
    que.append((row,col))
    visited[row][col] = True
    # print(row,col)
    while que:
        c_row, c_col = que.popleft()
        visited[c_row][c_col] = True
        for i in range(4):
            n_row = c_row + d_row[i]
            n_col = c_col + d_col[i]


            if not(0<=n_row<100 and 0<=n_col<100):
                continue
            
            if miro_map[n_row][n_col] == 1:
                continue

            if miro_map[n_row][n_col] == 0 and visited[n_row][n_col] == False:
                que.append((n_row,n_col))
            elif miro_map[n_row][n_col] == 3 and visited[n_row][n_col] == False:
                return 1
    return 0


for _ in range(10):
    tc = int(input())
    miro_map = [list(map(int,input().strip())) for _ in range(100)]

    visited = [[False]*100 for _ in range(100)]
    result = search_goal(1,1)

    print(f'#{tc} {result}')