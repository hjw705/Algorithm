# 문제: 위에서 아래로 (이코테)
# 문제설명: 내림차순 정렬
# 풀이법: sort 쓰기
# 느낀점: 흠,,그냥 내림차순 정렬
import sys
n = int(sys.stdin.readline())
nums_list = []
for i in range(n):
    n = int(sys.stdin.readline())
    nums_list.append(n)
nums_list = sorted(nums_list, reverse= True)
for i in nums_list:
    print(i, end= ' ')