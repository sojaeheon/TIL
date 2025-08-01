import sys
sys.stdin = open("input.txt", "r")

T = int(input())

# 비트로 변환할 숫자와 위치를 받을 bit_n
def binary_representation(number,bit_n):

    # 2진수로 변환
    num = list(format(number,'b'))

    # 찾는 수보다 변환된 2진수의 개수가 적으면 OFF
    if len(num) < bit_n:
        return "OFF"
    else:
        # 뒤에서부터 bit_n까지 1인지 판별
       for _ in range(bit_n):
           # 1이 아니면 OFF
            if num.pop() != "1":
                return "OFF"
    return "ON"



for tc in range(1,T+1):
    n, m = map(int,input().strip().split())

    result = binary_representation(m,n)

    print(f'#{tc} {result}')