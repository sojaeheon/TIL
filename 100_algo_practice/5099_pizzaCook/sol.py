import sys
from collections import deque
sys.stdin = open("sample_input.txt", "r")

def fire_pit(pit_num,num,pizzas_arr):
    que = deque()
    pizza_count = num
    while True:
        if len(que)==3:
            pop_num = que.popleft()[1] - pit_num + 1
            pop_num = pop_num//2
            if pop_num > 0:
                pizzas_arr.append(pop_num)
            else:
                pizza_count -= 1
        else:
            if len(que) == 1 and not pizzas_arr:
                return que.popleft()[0]
            else:
                que.append(pizzas_arr.popleft())

T = int(input())

for tc in range(1,T+1):
    n,m = map(int,input().strip().split())
    arr = list(map(int,input().strip().split()))

    pizzas = deque()
    for (idx,pizza) in enumerate(arr):
        pizzas.append((idx+1,pizza))

    result = fire_pit(n,m, pizzas)

    print(f'#{tc} {result}')