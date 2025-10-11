numbers = {
    '0001101' : 0,
    '0011001' : 1,
    '0010011' : 2,
    '0111101' : 3,
    '0100011' : 4,
    '0110001' : 5,
    '0101111' : 6,
    '0111011' : 7,
    '0110111' : 8,
    '0001011' : 9
}

T = int(input())

for tc in range(1, T+1):
    n, m = map(int,input().strip().split())
    arr = [input().strip().split() for _ in range(n)]
    password = []
    for row_data in arr:
        if '1' not in row_data:
            continue
        for col in range(m-1,0,-1):
            if row_data[col] == '1':
                end = col
                break
        for idx in range(end-55,end +1 , 7):
            num = row_data[idx:idx+7]
            password.append(numbers[num])
    total_sum = 0
    for i in range(0, 8):
        if i % 2 == 0:
            total_sum += (password[i]*3)
        else:
            total_sum += password[i]
    
    if total_sum % 10 == 0:
        print(f'#{tc} {sum(password)}')
    else:
        print(f'#{tc} {0}')


