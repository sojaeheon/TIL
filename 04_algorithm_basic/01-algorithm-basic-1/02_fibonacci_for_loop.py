def fibonacci_for_loop(n):

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        first, second = 0, 1
        for _ in range(2,n+1):
            next_fib = first + second
            first, second = second, next_fib
    return second

# 사용 예시
print(fibonacci_for_loop(10)) # 55