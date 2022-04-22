# 음료수 얼려먹기 (이코테)
# 문제: 0일 경우 아직 방문 안함 / 1이면 방문한 상태니깐 pass / n,m 크기 벗어날 경우 pass
# 풀이 : 재귀를 사용하는 DFS
# 느낀 점: readline() 사용할때 rstrip() 습관화하자 (\n 도 받으니깐 공백제거 필수!)

import sys
n,m = map(int, sys.stdin.readline().split()) # n,m 의 크기 입력받기
ice_list = []

for i in range(n):
    tmp = sys.stdin.readline().rstrip()
    ice_list.append(list(map(int,tmp))) # 얼음 리스트 입력받기

def dfs(x,y):

    if x < 0 or y < 0 or x >= n or y>= m:
        return False

    if ice_list[x][y] == 0: # 아직 방문하지 않았을 경우 방문처리
        ice_list[x][y] = 1
        # 상하좌우
        dfs(x - 1, y)  # 상
        dfs(x + 1, y)  # 하
        dfs(x, y - 1)  # 좌
        dfs(x, y + 1)  # 우

        return True

    return False # 방문했을 경우 종료

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1

print(result)