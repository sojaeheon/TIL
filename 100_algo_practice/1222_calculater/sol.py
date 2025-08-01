import sys
sys.stdin = open("input.txt", "r")

def infix_to_postfix(input_cal):
    op_dict = {'+':1,'-':1,'*':2,'/':2,'(':0}
    stack = []      # 연산자를 저장할 스택
    postfix = []    # 후위 표기식을 저장할 리스트

    for char in input_cal:
        if char.isnumeric():        # 정수라면
            postfix.append(char)    # 후위표기식에 삽입
        elif char == '(':
            stack.append(char)
        elif char == ')':
            top_token = stack.pop() # 연산자들을 스택에서 빼기
            while top_token != '(': # 여는 소괄호를 만날때까지
                postfix.append(top_token)
                top_token = stack.pop()
        else:       # 연산자인 경우
            # 스택에 있는 연산자들이 지금 검사하는 연산자보다
            # 우선순위가 높거나 낮을 때 서로 다르게 처리해야한다
            while stack and op_dict[stack[-1]] >= op_dict[char]:
                postfix.append(stack.pop())
            stack.append(char)
    while stack:
        postfix.append(stack.pop())

    return postfix

def calculator(x,y,oper):
    if (oper == '+'):
        return x + y
    elif (oper == '-'):
        return x - y
    elif (oper == '*'):
        return x * y
    elif (oper == '/'):
        return x / y

def run_calculator(postfix_cal):
    op_set = ('+','-','/','*')
    stack = []
    operator = []

    while postfix_cal:
        c = postfix_cal.pop()
        # 연산자인 경우
        if c in op_set:
            operator.append(c)
        # 정수일 때
        elif c.isnumeric():
            if not stack: # stack에 숫자가 없을 때
                stack.append(c)
            else:           # stack에 숫자가 있을 때
                a = stack.pop() # stack에서 숫자 하나 빼기
                op = operator.pop() # 저장된 연산자 하나 빼기
                b = c   # 현재 숫자 저장
                result = calculator(int(a),int(b),op) # 계산함수 호출
                stack.append(result)    # 계산된 값 stack에 다시 넣기

    while len(stack)>1:        # 스택에 숫자가 남아있을 경우
        a = stack.pop()  # stack에서 숫자 하나 빼기
        op = operator.pop()  # 저장된 연산자 하나 빼기
        b = c  # 현재 숫자 저장
        result = calculator(a, b, op)  # 계산함수 호출
        stack.append(result)

    return stack[0]

T = 10

for tc in range(1,T+1):
    str_len = int(input())
    input_cal = input().strip()

    postfix_expression = infix_to_postfix(input_cal)
    answer = run_calculator(postfix_expression)

    print(f'#{tc} {answer}')
