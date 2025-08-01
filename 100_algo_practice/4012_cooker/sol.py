import sys
sys.stdin = open("sample_input.txt", "r")


T = int(input())

for tc in range(1,T+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]

    result = cook(arr,n)






