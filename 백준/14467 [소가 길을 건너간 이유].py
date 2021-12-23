# 백준 14467 - 소가 길을 건너간 이유
# 문제 설명 : 소의 번호와 소의 위치가 주어지며 같은 번호의 소가 위치를 바꾼 것이 몇번인지 구하기
# 접근 방법 : 1~10번까지의 소의 위치 저장할 빈 리스트 선언 / 소의 이전 위치 저장해주는 변수와 새로 입력된 위치 비교하며, 다를 경우 count 증가
# 어려웠던 점: 문제푸는 방식이 다양할 수 있으나, 딕셔너리 쓰면 좀 복잡하게 느껴져서 결국 다른 풀이 찾음

import sys
n = int(sys.stdin.readline())

# 소들의 위치를 저장하는 리스트 변수 선언
# 소의 번호가 1이상 10이하의 정수이므로, 10번까지 있음
cows = [None] * 10

# 소가 길을 건너간 최소 횟수를 저장할 변수 선언
count = 0

for i in range(n):
    # 소의 번호와 위치를 공백으로 구분해 입력
    cowNum, location = map(int,sys.stdin.readline().split(' '))

    # 소의 이전 위치를 저장하는 변수 선언
    prev_cow_location = cows[cowNum - 1]

    # 이번에 입력된 소의 번호에 입력된 위치로 초기화해주기
    cows[cowNum - 1] = location

    # 소의 위치가 None 이 아니면서, 이전의 위치와 현재의 위치가 다를 경우
    if prev_cow_location != None and prev_cow_location != location:
        # 소가 이동한 것이므로 count 에 1 더해주기
        count += 1

print(count)




