import sys
sys.stdin = open("input.txt", "r")


def run_triplet_check(arr):
    return (arr[0]+1 == arr[1] == arr[2]-1) or (arr[0] == arr[1] == arr[2])

def baby_jin(current_cards,remain_cards):
    global baby_jin_check

    if len(current_cards) == 3 and len(remain_cards) == 3:
        if run_triplet_check(current_cards) and run_triplet_check(remain_cards):
            baby_jin_check = False
        return

    else:
        for i in range(len(remain_cards)):
            if baby_jin_check:
                select_i = remain_cards[i]
                remain_list = remain_cards[:i] + remain_cards[i+1:]
                baby_jin(current_cards + [select_i],remain_list)
            else:
                return

T = int(input())

for tc in range(1, T+1):
    cards = list(map(int,list(input().strip())))
    baby_jin_check = True

    baby_jin([],cards)

    if baby_jin_check:
        print(f'#{tc} false')
    else:
        print(f'#{tc} true')




