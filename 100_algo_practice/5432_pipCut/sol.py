import sys
from collections import deque
sys.stdin = open("sample_input.txt", "r")

T = int(input())

def pipe_cut(arr):
    count = 0
    stack = []
    before_char = ''
    while arr:
        pipe_pop = arr.popleft()
        if pipe_pop == '(':
            stack.append(pipe_pop)
        else:
            stack.pop()
            if before_char == ')':
                count+=1
            else:
                count += len(stack)
        before_char = pipe_pop


    return count

for tc in range(1,T+1):
    pipe = deque(list(input().strip()))

    result = pipe_cut(pipe)
    print(f'#{tc} {result}')
