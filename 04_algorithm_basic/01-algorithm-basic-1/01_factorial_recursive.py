'''
    재귀함수 2가지 룰
    1. Basis Rule : 1이 되었을 때는 1을 반환해야한다
    2. Inductive Rule: (n-1)로 자기 자신을 호출
'''
def fact(n):
    if n==1:
        return 1
    return n * fact(n-1)


# 사용 예시
print(fact(5))  # 5*4*3*2*1을 계산하여 120을 출력합니다
