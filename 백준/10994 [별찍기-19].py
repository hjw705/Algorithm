# 백준 10994 - 별찍기 19
# 문제 설명 : 예제를 보고 규칙 유추 후 별 찍기

# 접근 방법 : # 1) 재귀
# n = 1 일 경우, 4 * n - 3 = 1
# n = 2 일 경우, 4 * 2 - 3 = 5
# n = 3 일 경우, 4 * 3 -3 = 9
# n = 4 일 경우, 4 * 4 - 3 = 13
# 가장 왼쪽 가장자리에 있는 네모의 * 이 가로 2, 세로 (아래) 2만큼 가면 새로운 네모의 가장자리가 나옴
# 가장 왼쪽 가장 자리 좌표를 (x,y) 로 생각하기

# 어려웠던 점: 별의 갯수가 변하는 규칙성은 찾아냈으나, 별의 좌표에 따른 이동을 어떻게 해야 하는지 감을 못 잡음 / 별의 갯수가 변하는 규칙성에 따른 식을
#           세우는 데 어려웠음

import sys

def answer(n, idx):
    if n == 1:
        recMap [idx][idx] = '*'
        return;
    l = 4 * n - 3

    for i in range(idx, l+idx):
        # 위 아래
        recMap [idx][i] ='*'
        recMap [idx+l-1][i] = '*'

        # 양 옆
        recMap [i][idx] ='*'
        recMap [i][idx+l-1] ="*"

    return answer(n-1, idx+2)

n = int(sys.stdin.readline())

# 입력받은 수에 따른 사각형의 길이
lens = 4 * n - 3

# 빈 이차원 배열 만들어 주기
recMap = [[' '] * lens for _ in range(lens)]

answer(n,0)

# 결과 출력
for i in range(lens):
    for j in range(lens):
        print(recMap[i][j], end = '')
    print()