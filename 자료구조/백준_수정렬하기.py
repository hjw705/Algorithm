# 수정렬하기 백준 2750번
import sys
sys.setrecursionlimit(10**7)

N =  int(input()) #입력받을 숫자의 개수
nums_list = [] #빈 리스트

for i in range(N):
    s = int(input()) #입력받을 수의 개수만큼 입력받기
    nums_list.append(s) #입력받은 수 빈 리스트에 저장자

def quick_sort(nums_list):
    if len(nums_list) <= 1:
        return nums_list
    pivot = nums_list[0]
    tail = nums_list[1:]

    left_list = [x for x in tail if x <= pivot]
    right_list = [x for x in tail if x > pivot]

    return quick_sort(left_list) + [pivot] + quick_sort(right_list) #유의사항: 같은 형태만 더해질수 있는거 있지 말기

#큌소트 정렬한 리스트에 있는 값 출력
for i in quick_sort(nums_list):
    print(i)
