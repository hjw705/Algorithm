# 문제 : (구현) 백준 최소 최대 2
# 문제 설명 : 첫번째 줄 - 입력받을 테스트 케이스 갯수 / 두번째 줄 이후부터 테스트케이스의 개수만큼 입력받을 정수 갯수 & 정수들 /
# 접근 방법 : 그냥 일반적인 구현 문제라 딱히 접근 방법 없음
# 느낀 점: 처음에 if 절 안쓰고 min() max() 쓰니깐 "ValueError: max() arg is an empty sequence"
# 경고문 나옴 / min max 쓸는 무조건 !! if 문 써야 이런 에러 안나온다 함

import sys
test_num = int(sys.stdin.readline()) # 입력받을 테스트 갯수

for i in range(test_num): # 입력받은 테스트 갯수만큼
    n = int(sys.stdin.readline()) # 입력받을 정수둘의 수
    nums = list(map(int, sys.stdin.readline().split())) # 입력받을 정수 리스트
    if len(nums) > 0:
        print(min(nums),max(nums)) # 최소값, 최댓값 출력