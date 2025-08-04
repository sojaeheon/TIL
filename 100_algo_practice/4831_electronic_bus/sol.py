import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    # k 충전을 해야 종점에 도착할 수 있는지 출력하는 프로그램
    # n = 정류장 개수
    # m = 충전기가 설치된 정류장 수
    K, N, M = map(int,input().strip().split())
    charging_machine = list(map(int,input().strip().split()))
    machines = [False] * N

    charge_count = 0

    for idx in range(M):
        machines[charging_machine[idx]] = True
    
    current_idx = 0

    while True:
        current_idx +=K
        if current_idx > N-1:
            break
        # 현재 위치에 충전기가 있으면
        if machines[current_idx]:
            charge_count += 1
        else:
            for _ in range(K-1):
                current_idx -= 1
                if machines[current_idx]:
                    charge_count+=1
                    break
            else:
                break
    
    if current_idx < N:
        charge_count = 0

    print(f'#{tc} {charge_count}')


            
    