

def partition(arr,start,end):
    p = arr[start]
    left = start+1
    right = end

    while True:
        while left <= end and arr[left]<p:
            left+=1
        while right > start and arr[right]>p:
            right-=1
        if left<right:
            arr[left],arr[right] = arr[right], arr[left]
        else:
            break
    
    arr[start], arr[right] = arr[right], arr[start]
    return right
    
def quick_sort(arr,start,end):
    if start<end:
        p = partition(arr,start,end)

        quick_sort(arr,start,p-1)
        quick_sort(arr,p+1,end)


T = int(input())

for tc in range(1,T+1):
    n = int(input())
    a = list(map(int,input().strip().split()))

    quick_sort(a,0,n-1)

    print(f'#{tc} {a[n//2]}')