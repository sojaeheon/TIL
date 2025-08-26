import sys
sys.stdin = open('input.txt')

'''
 정수 i를 부분 집합에 포함시킬지 고려할 때 
 이미 부분 집합에 포함시킨 원소의 합 S와 
 아직 고려하지 않은 숫자들의 합 R
 을 동시에 활용하면 시간을 단축할 수 있다고 한다.
'''


# 결국, 부분집합의 합을 만들기 위한 아이디어 -> 비트 연산 하던것과 다를바 없다.
    # 0번째 요소를 쓴 경우,
    # 0번쨰 요소를 안 쓴 경우
def DFS(idx, acc, remain):
    '''
        idx: 현재 조사중인 대상의 index
        acc: 현재까지 누적된 값
    '''
    global result
    # 가지치기
    # 누적값이 K를 초과한 순간, 양의 정수로만 모인 원소들로는
    # 다시는 K가 될 가망 없음
    if acc > K:
        return  # 조사 종료

    # 이 조사를 왜 하는데?
    if acc == K:        # 그 요소를 선택하느냐 마느냐로 만들어진 누적값이 K가 된경우
        # 가능한 경우 1 증가
        result += 1
        return          # 다음 조사 막는다.

    # 이 조사를 언제까지 할건데?
    # 조사 대상 넘버가 전체 N보다 커지면 안됨
        # 지금까지의 누적값 + 남아있는 모든 수의 합
            # 그 값이 목표치 K에 도달할 수 없다!
            # 조사의 의미가 없다.
    if idx >= N or acc + remain < K:
        return  # 조사 불가능
    
    # 다음 대상으로 조사 시작! 하는 구간
    '''
        이전까진 acc + nums[idx] 를 사용해서 idx 번쨰의 값을 더했다!
        nums[idx] 번째를 사용했다는 의미이므로,
        remain(사용하지 않은 값들의 합) 에서는 nums[idx] 번째 값 만큼 빼기
    '''
    DFS(idx + 1, acc+nums[idx], remain-nums[idx])   # DFS 호출시, 누적값에 idx 번째 요소르 더한 경우,
    # nums[idx] 번쨰 값을 사용하지 않겠다! 라고 선언한 경우,
    # remain(사용하지 않은 값들의 합) 에서도 nums[idx] 를 빼 줘야 한다.
        # 이제부터, nums[idx] 번쨰는 우리의 누적합에 영향을 끼쳐선 안되기 떄문에.
    DFS(idx + 1, acc, remain-nums[idx])            # DFS 호출시, 누적값에 idx 번째 요소르 더하지 않은 경우,

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    # 1부터 N까지의 정수 배열
    nums = list(range(1, N+1))
    result = 0  # 부분집합의 원소의 합이 K가 되는 경우가 있으면 1씩 증가
    # 시작 인덱스는 0으로
    # 시작 누적값은 0으로
    # 시작 나머지 값은 nums의 전체합
    DFS(0, 0, sum(nums))
    print(result)