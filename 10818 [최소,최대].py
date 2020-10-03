n=int(input()) #첫번째 줄 정수 N개 입력받기
nums_list = [int(n) for n in input().split()]#두번째 줄 정수 N개 만큼 정수입력받고 리스트에 넣기
nums_list.sort()
print(nums_list[0],nums_list[n-1])