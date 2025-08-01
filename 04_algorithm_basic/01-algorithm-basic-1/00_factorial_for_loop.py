# 팩토리얼을 반복문으로 구현!

n = int(input())
fac = 1
for i in range(2,n+1):
    fac *=i

print(fac)