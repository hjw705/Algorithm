# 이코테 BFS 코드
from collections import deque

def bfs(graph, start, visited):
  queue = deque([start]) # 시작 노드를 큐에 넣어줌
  visited[start] = True # 현재 노드를 방문 처리
  while queue: # 큐가 빌때까지 반복
    v = queue.popleft()  # 큐에서 하나의 원소를 뽑아 출력
    print(v, end=' ')
    for i in graph[v]: # 꺼낸 노드와 인접한 노드들 중에 아직 방문하지 않은 것을 큐에 넣어주고 방문처리
      if not visited[i]:
        queue.append(i)
        visited[i] = True

# 각 노드가 연결된 정보를 2차원 리스트 형태로 표현
graph = [

  [],
  [2,3,8],
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]

# 각 노드가 방문된 정보를 1차원 리스트로 표현
visited = [0] * 9

bfs(graph, 1, visited)