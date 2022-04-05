# 백준 1978 - 소수찾기 (수학)
# 문제 설명: 첫줄에 수의 갯수 / 두번째 줄 수의 개수만큼 입력받는 숫자들
# 접근 방법: 소수 판별 알고리즘 사용

import sys
import math
n = int(sys.stdin.readline()) # 수의 개수
nums_list = list(map(int,sys.stdin.readline().split())) # 입력받는 숫자들
cnt = 0 # 소수의 개수

# 소수 판별 함수
def is_prime(x):
    if x <= 1:
        return False
    for i in range(2,int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

# 입력받은 숫자 리스트 안에 있는 숫자들 하나하나 소수 판별
for i in nums_list:
    if is_prime(int(i)):
        cnt += 1
        continue

print(cnt)
