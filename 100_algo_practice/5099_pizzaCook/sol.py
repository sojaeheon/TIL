import sys
from collections import deque
sys.stdin = open("sample_input.txt", "r")

def fire_pit(pit_num,num,pizzas_arr):
    que = deque()
    
    for _ in range(pit_num):
        que.append(pizzas_arr.popleft())
    
    while len(que)>1:
        idx, cheese = que.popleft()
        cheese//=2
        if cheese == 0:
            if pizzas_arr:
                que.append(pizzas_arr.popleft())
        else:
            que.append((idx,cheese))

    return que[0][0]
T = int(input())

for tc in range(1,T+1):
    n,m = map(int,input().strip().split())
    arr = list(map(int,input().strip().split()))

    pizzas = deque()
    for (idx,pizza) in enumerate(arr):
        pizzas.append((idx+1,pizza))

    result = fire_pit(n,m, pizzas)

    print(f'#{tc} {result}')