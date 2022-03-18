# 백준 9934 - 완전이진트리
# 문제 설명: 압력 - 이진트리의 깊이 k, 두번째 줄은 방문한 빌딩의 번호들 / 출력 - 레벨 번호 i, i레벨에 해당하는 빌딩의 번호 (이때 루트노드 의 레벨은 0임)
# 해결 방법: inorder 방식으로 노드를 채워나감 (L -H - R) / 노드 채워 나가는 코드 구현 /
# 어려운 점: 루트 구하는 코드 위치에 따라 나오는 정답이 달라졌음 (얘 먼저 항상 쓰자)
# 보완할 점: inorder 할때 가운데를 기준으로 왼쪽/ 오른쪽 나눠서 풀었으면 더 쉬웠을 듯 / 배열 중간값이 루트

import sys
k = int(sys.stdin.readline()) # 이진트리의 깊이 k
build_num = list(map(int,input().split()))# 리스트에 빌딩 번호들 저장
answer = [[] for _ in range(k)] # 각각의 depth 에 담을 번호 리스트

def inorder(build_num, depth):
    mid = len(build_num) // 2  # 루트 노드
    answer[depth].append(build_num[mid])  # 루트노드 깊이에 해당하는 배열부터 채워나가기
    if len(build_num) == 1: # 더 이상 남아있는 빌딩 번호들이 없을 경우 return
        return
    inorder(build_num[:mid], depth+1) # 왼쪽 트리
    inorder(build_num[mid+1:], depth+1) # 오른쪽 트리

inorder(build_num, 0)  # 루트 노드부터 채워 나가기 시작

for i in range(k):
    print(*answer[i]) # list = [1,2,3,4] 일때 print(*list) -> 리스트에 있는 값 한줄에 출력 가능한 문법 (1 2 3 4)