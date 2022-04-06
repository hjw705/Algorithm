# 이코테-구현-상하좌우
# 문제 설명: 첫번째줄 : 공간의 크기 N / 두번째 줄: 상(U) 하(D) 좌(L) 우(R) 입력받은 후 좌표 결과값 출력
# 접근 방법: 반복문 돌면서 if 문 따라서 LRUD 수행 => 이코테 책에 나와있는 풀이 대로 고침
# 어려웠던 점: 방향 벡터가 익숙하지 않았음 / 입력받은 이동 계획 하나씩 확인 하는 반복문 수행 후, 정해진 이동게획의 종류 하나씩 확인하는 반복문

import sys
n = int(sys.stdin.readline()) # 공간의 크기
plans = sys.stdin.readline().split() # 입력받은 이동계획들

x,y = 1,1 # 초기 좌표값

# 동,북,서,남
dx = [0,0,-1,1] # 행
dy = [-1,1,0,0] # 열
move = ['L','R','U','D'] # 이동 계획

for plan in plans: # 입력받은 이동 계획 하나씩 확인
    for i in range(len(move)): # 정해진 이동게획의 종류 하나씩 확인
        if plan == move[i]: # 입력받은 이동계획과 정해진 이동계획의 종류 중 같은게 있다면
            nx = x + dx[i] # 해당 이동게획에 맞는 좌표 이동
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n : # 초기 좌표값이 1,1 이며, 해당 좌표값을 벗어나지 않도록 하기
        continue # 이어서 위에 있는 반복문 수행
    x, y = nx, ny

print(x,y)
