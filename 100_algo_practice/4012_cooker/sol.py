# n 개의 식재료가 있다
# 식재료들을 각각 N/2개씩 나누어 두 개의 요리를 하려고 한다(N은 짝수)
# 이때, 각각의 음식을 A음식, B음식이라고 한다

# 식재료 1<= i <= N, 1<=k<=N, i != j
# 4<= N <= 16
# 1 <= sij <= 20,000, i != j

import sys
sys.stdin = open("sample_input.txt", "r")

def food_value(idx_list, S):
    """idx_list에 든 재료들의 시너지 합 (i != j인 모든 순서쌍 합)"""
    total = 0
    L = len(idx_list)
    for a in range(L):
        i = idx_list[a]
        for b in range(L):
            j = idx_list[b]
            if i != j:
                total += S[i][j]
    return total


def dfs(add_ingre, remain, limit):

    global min_result

    if limit == 0:
        # A음식 = add_ingre
        A = add_ingre
        # B음식 = 전체 재료 - A
        B = [x for x in ingredients if x not in A]

        valA = food_value(A, arr)
        valB = food_value(B, arr)
        diff = abs(valA - valB)
        
        if diff < min_result:
            min_result = diff
        
        return
    
    for i in range(len(remain)):
        dfs(add_ingre + [remain[i]], remain[i+1:], limit - 1)
    


T = int(input())

for tc in range(1,T+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    visited = [True]*n

    min_result = 20000*16

    cook_count = n//2

    ingredients = [i for i in range(n)]

    dfs([],ingredients,cook_count)

    print(f'#{tc} {min_result}')





