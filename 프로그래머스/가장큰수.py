# 문제: 프로그래머스 가장 큰수 (level 2)
# 문제설명: 매개변수로 정수들이 담긴 리스트가 주어졌을 때 만들어질수 있는 숫자 조합들 만듦 / 그중 가장 큰 숫자를 문자열 형태로 출력
# 풀이법 : 입력받은 정수 리스트들 조합으로 모든 순열 조합들 만들기 / 이후 선택정렬로 정렬 후 가장 큰 값 찾기
# 느낀점 :
# 1) permutations 썼는데 처음에 시간초과남 킹받네;;
# 2) 파이썬 lambda 사용하면 개쉬워짐 그리고 숫자 범위 주는 조건문 봐야함 ㅎ 보면 쉽게 푸는 힌트 얻을 수 있음
# 3) 문자열은 아스키 값을 치환됨
# '666' -> 86 86 86
# '101010' -> 81 80 81 80 81 80
# '222' -> 82 82 82
# 따라서 6 > 2 > 1 순으로 큼
# 4) sort 의 기본정렬은 오름차순임
# 참고: https://wooaoe.tistory.com/82

# ---------------내가 만든 시간복잡도 졸라 높은 코드-----------------------
# from itertools import permutations
# def solution(numbers):
#     perm_list = []
#     tmp_list=[]
#     result = []
#
#     # 매개변수로 입력받은 문자열 리스트 순열로 다양하게 조합된 문자열 만들기
#     for i in permutations(numbers):
#        perm_list.append(list(map(str,i)))
#
#     # 조합된 문자열들이 큰리스트안에 각각의 리스트로 들어가있는데,그 각각의 리스트 안에서 문자열 합치기 해줌 / 각각의 하나의 문자열이 담긴 리스트로 만들어주기
#     for i in range(len(perm_list)):
#         for j in range(len(perm_list[i])):
#             tmp_list.append(''.join (perm_list[i]))
#
#     # 문자열 담긴 리스트를 정수로 바꿔서 max 값 구하고 다시 문자열로 바꿔주기
#     for i in tmp_list:
#         result.append(int(i))
#     return (str((max(result))))
#
# print(solution([6,10,2]))
#------------------------------------------------------------

def solution(num):
    num= list(map(str,num)) # 입력받은 int형 리스트 문자열로 변환
    num.sort(key =  lambda x : x*3, reverse=True) # 문제 조건에서 numbers의 원소는 0이상 1000이하라 함 따라서 3자리수로 맞춘후 비교하겠다는 것

    return str(int(''.join(num))) # 모든 값이 0일때 '000'을 처리해주기 위해 int로 변환 후 다시 str 로 바꿔줌