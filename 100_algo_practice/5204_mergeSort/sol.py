

def merge_sort(arr):
    
    if len(arr)<=1:
        return arr
    mid = len(arr)//2
    left_arr = merge_sort(arr[0:mid])
    right_arr = merge_sort(arr[mid:])

    if left_arr and right_arr and left_arr[-1]>right_arr[-1]:
        result.append(left_arr[-1])

    l, r = 0, 0
    temp_arr = []

    while l<len(left_arr) and r<len(right_arr):
        if left_arr[l] <= right_arr[r]:
            temp_arr.append(left_arr[l])
            l+=1
        else:
            temp_arr.append(right_arr[r])
            r+=1
    if l<len(left_arr):
        temp_arr += left_arr[l:]
    if r<len(right_arr):
        temp_arr += right_arr[r:]
    
    return temp_arr

# 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우 출력

T = int(input())

for tc in range(1,T+1):
    n = int(input())
    arr = list(map(int,input().strip().split()))

    result = []

    arr_result = merge_sort(arr)

    if result:
        print(f'#{tc} {arr_result[n//2]}',len(result))
    else:
        print(f'#{tc} {arr_result[n//2]} 0')