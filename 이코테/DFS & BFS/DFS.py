# 이코테 DFS 코드
def dfs(graph, v, visited):
  visited[v] = True # v 번호에 해당하는 노드 방문했을 경우
  print(v,end='') # 그 번호 출력

  for i in graph[v]: # 방문한 그래프 노드 도는 데
    if not visited[i]: #방문하지 않은 것이라면
      dfs(graph,i,visited) # 해당 노드와 연결된 노드들 그래프 안에서 방문하기

# 그래프는 2차원 리스트로 표현 가능
graph = [
  [] ,# 0번째 인덱스는 비어있음
  [2,3,8], #1번 노드와 연결된 건 3,8번 노드
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]

# 처음에 노드들 싹 다 비워두기
visited = [False]* 9

dfs(graph,1,visited)