# 문제 : 이코테 (음료수 얼려 먹기)
# 문제 설명: 얼음틀(0,1 로 구성된) 모양이 주어질 때 생성되는 총 아이스크림 개수 구하는 문제 / 연결요소의 갯수 구하기
# 풀이법: DFS / 시작하는 곳을 기점으로 만약 상하좌우 방향애서 같은 숫자일 경우, 방문처리 / 아닐 경우 0 처리
# 느낀점: 구현문제 에전에 풀었던거랑 뭔가 유사한 느낌 / 좌표 개념 잘 알아두는 게 중요한 듯 하다

import sys
n,m = map(int, sys.stdin.readline().split()) #행 열 숫자 입력
ice = []
for i in range(m-1): # 얼음 틀 입력받기
    ice.append(list(map(int, input())))

def dfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y>=m: # 주어진 범위를 벗어날 경우
        return False
    if ice[x][y] == 0 : # 방문하지 않은 노드일 경우
        ice[x][y] = 1 # 방문처리
        dfs(x+1,y) # 상
        dfs(x-1,y) # 좌
        dfs(x,y+1) # 하
        dfs(x,y-1) # 우
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True: # 현재 위치에서 DFS 수행앴는데 방문이 된것일 경우
            result += 1 #count 함

print(result)