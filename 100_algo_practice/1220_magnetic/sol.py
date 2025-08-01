import sys
sys.stdin = open("input.txt", "r")

T = 10

def deadlock(arr,num):
    deadlock_count = 0

    for i in range(num):
        check = False
        for j in range(num):
            if arr[j][i] == 1:
                check = True
            elif check and arr[j][i] == 2:
                deadlock_count +=1
                check = False
    return deadlock_count


for tc in range(1,T+1):
    n = int(input())
    arr = [list(map(int,input().rstrip().split())) for _ in range(n)]

    result = deadlock(arr,n)

    print(f'#{tc} {result}')