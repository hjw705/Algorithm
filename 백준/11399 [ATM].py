# 백준 11399 - ATM
# 문제 설명 : 1대의 atm 에 n명의 사람이 줄을 섰을 때, m번째 사람이 돈을 인출시 걸리는 시간은 Pm,
#           모든 사람이 대기시간을 합쳐 모두 돈을 인출시에 걸리는 최소의 시간 구하기
# 접근 방법 : 입력받은 리스트 p가 오름차순이어야 대기시간이 짧아져 걸리는 최종 시간이 최소로 나옴
# 어려웠던 점: 처음에 입력받을 정수의 갯수 입력 후, 정수들 리스트 입력받는데, 이걸 입력받을 정수의 갯수 만큼의 반복문을 돌면서 리스트 입력 받으려 하니 골치아파짐

import sys
n = int(sys.stdin.readline())
p = list(map(int,input().split()))
p.sort()

sum = 0
result = 0
for i in range(n):
    sum += p[i]
    result += sum

print(result)