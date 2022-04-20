# 문제 : 이코테 (미로 탈출)
# 문제 설명: 괴물이 있는 곳은 0, 없는 곳은 1 / 1로 이루어진 부분만 방문가능할 때 (1,1) 자리에서 마지막
# (n,m)까지의 좌표까지 갈때까지의 최소한의 거리 구하기
# 풀이법: BFS를 통해 가장 인접한 1로 이동하여 최소의 거리 구하기
# 느낀점: "최단" 거리 구할때 BFS 가 좋은 듯

from collections import deque
import sys
n,m = map(int,sys.stdin.readline()) # 행, 열 개수 입력받기
graph = []

# n개 만큼의 리스트 맵 입력받기
for i in range(n):
    graph.append(list(map(int,sys.stdin.readline())))

# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    # 큐가 빌때까지
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <0 or ny<0 or nx >=n or ny>=m:
                continue

            # 괴물 만날 경우
            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append(nx,ny)

    return graph[n-1][m-1] # 가장 오른쪽 아래 좌표까지 최단 거리 반환

print(bfs(0,0))
