import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    
    # 10x10 도화지: 색 정보 저장 (0:없음, 1:빨강, 2:파랑, 3:보라)
    paper = [[0]*10 for _ in range(10)]

    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                # 빨강(1) 또는 파랑(2)가 있으면 더함 (겹치면 3이 됨)
                if paper[i][j] == 0:
                    paper[i][j] = color
                elif paper[i][j] != color:
                    paper[i][j] = 3  # 보라색

    # 보라색(3)인 칸의 개수 세기
    result = 0
    for i in range(10):
        for j in range(10):
            if paper[i][j] == 3:
                result += 1

    print(f"#{tc} {result}")

  

