import sys
sys.stdin = open("input.txt", "r")

from collections import deque

def make_password(arr):
    num = 1
    while True:
        if num == 6:
            num = 1
        first_num = arr.popleft() - num
        if first_num <= 0:
            arr.append(0)
            break
        else:
            arr.append(first_num)
        num+=1
    return arr


for _ in range(10):
    tc = int(input())
    numbers = deque(map(int,input().strip().split()))

    result = make_password(numbers)

    print(f'#{tc}', *result)