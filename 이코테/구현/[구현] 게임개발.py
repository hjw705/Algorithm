# 문제 이코테- 구현- 게임개발

# 문제 설명 : 첫번째줄 입력 - 세로크기 N, 가로크기 M을 공백으로 구분하여 입력
# 두번째 줄 입력 - 현재 캐릭터가 있는 칸의 좌표 (A,B) 와 바라보는 방향 d 공백으로 입력
# 이때 d는 0아면 북쪽 / 1이면 동쪽 / 2이면 남쪽 / 3이면 서쪽
# 세번째줄 부터의 입력 - NXM 의  리스트 입력 받음 (0이면 육지 / 1이면 바다)
# 이때 바다일 경우, 접근안함 / 처음 캐릭터 위치는 항상 육지
# 캐릭터가 방문하는 칸의 개수 출력하기

# 접근 방법 : 이코테에 나와있는 풀이법대로 함
# 느낀 점 : 국민카드 코딩테스트랑 매우 유사했다. 풀고 갔으면 더 좋았을 것 같다
# 추가로, map 이라는 이름의 리스트 만들었는데, 이러면 파이썬 문법 map이랑 혼동되어서 에러 남

import sys
row, col = map(int,sys.stdin.readline().split()) # N X M 크기의 맵
x,y,d = map(int, sys.stdin.readline().split()) # 캐릭터가 있는 좌표와 앞으로의 방향
dir = [0,3,2,1] # 북서남동
dx = [0,-1,0,1]
dy = [-1,0,1,0]

# 방문 좌표 저장하는 어레이
visit = [[0] * col for _ in range (row)]
visit [x][y] = 1 # 첫 좌표

# 전체 맵 정보 입력받기
map_list = []
for i in range(row):
    map_list.append(list(map(int,sys.stdin.readline().split())))

# 왼쪽으로 회전
def turn_left():
    global d
    d -= 1 # -1 빼주고
    if d < 0: # d가 0일때 -1이 되면 0보다 작은거니깐
        d = 3 # 서쪽 방향, 즉 왼쪽으로 초기화 해준다는 의미

count = 1 # 방문한 칸 횟수
dir_count = 0 # 몇번 방향 바꾸었는지 (4되면 한바퀴 돌았다는 의미)

while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[d]
    ny = y + dy[d]

    # * 문제에서 2번 조건
    # 회전한 이후 정면에 가보지 않은 칸이 있을 경우
    if visit[nx][ny] == 0 and map_list[nx][ny] == 0: # 바다가 아닌 경우
        visit[nx][ny] = 1 # 방문한 곳은 육지
        x,y = nx, ny
        count += 1 # 방문 횟수 +1
        dir_count = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다일 경우
    else:
        dir_count += 1

    # * 문제에서 3번 조건
    # 네개의 방향 다 갈 수 없을 경우
    if dir_count == 4:
        # 바라보는 방향 유지한 채 한칸 뒤로
        nx = x - dx[d]
        ny = y - dy[d]
        # 뒤로 갈 수 있다면 이동하기 (육지인 경우)
        if map_list[nx][ny] == 0:
            x, y = nx, ny
            dir_count = 0
        # 뒤가 바다로 막혀있는 경우
        else:
            break
print(count)







