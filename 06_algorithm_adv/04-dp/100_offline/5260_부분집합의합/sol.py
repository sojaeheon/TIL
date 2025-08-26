import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    # 1부터 N까지의 정수 배열
    nums = list(range(1, N+1))
    result = 0  # 부분집합의 원소의 합이 K가 되는 경우가 있으면 1씩 증가
    '''
        부분 집합의 합을 구할 수 있는 가장 간단한 방법
        1. 완전 검색
            -> bit 연산 사용하기
            -> N개의 원소로 만들수 있는 모든 부분집합의 경우의 수 
                2 ** N
            -> 1 << N
    '''
    for i in range(1 << N):     # 모든 경우의수 상황에 대해서 물어본다.
        tmp = 0                 # i번째 경우의 수에 사용된 요소들의 합
        tmp_arr = []
        for j in range(N):      # i번쨰 경우의 수에 j번 요소 썼니?
            '''
                i번째 요소 -> i = 7
                j번째 요소 -> 0~9 | 1을 j번 왼쪽으로 shift 한다는 뜻은?
                0 -> 0000000001
                1 -> 0000000010
                2 -> 0000000100
                ...
                0000000111 -> 7을 2진수로 변환 
                0000000001 -> 1을 j번 왼쪽으로 shift
                ----------  비트 and 연산
                0000000001 -> True  (7번째 경우의 수에는 0번쨰 요소가 사용되었다.)
            '''
            if i & (1 << j):
                tmp += nums[j]
                tmp_arr.append(nums[j])
            # 가지치기 가능할까?
            # 1부터 N까지의 모든 요소를 합해 나갈 건데...
            # 목표인 K를 이번 J번째 요소 더했을때 이미 초과헀다면... 더이상 조사할 의미 없지 않을까>
            if tmp > K: break
        # 모든 요소에 대해 사용여부 판별이 끝났다면
        if tmp == K:    # 전체 합이 K와 일치 하다면
            print(tmp_arr, end=' ')
            result += 1
    print(f'#{tc} {result}')