#level2_소수 찾기_완전탐색
# 문제설명 : 문자열을 하나씩 끊어서 숫자들로 만들기 / 숫자들로 만들수 있는 숫자 조합 여러개 만들기 / 조합 중 소수인거 개수 반환
# 접근방법: 1) 문자열 split / 2) 원소의 갯수에 해당하는 자릿수의 순열 만들기 + 튜플 중복 제거 / 3) 소수인거 판별 함수 구현
# 어려운점: 순열 리스트 join 하는 문법 생각해내지 못함

from itertools import permutations
import math

# 소수 판별 함수
def is_prime(x):
    if x <= 1:
        return False
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어 떨어진다면
        if x % i == 0:
            return False  # 소수가 아님
    return True

def solution(numbers):
    answer = [] #소수 갯수 담을 리스트
    for k in range(1, len(numbers)+1): #numbers 문자열 길이 만큼
        perlist = list(map(''.join, permutations(list(numbers), k))) #문자열 순열 리스트 합쳐진거
        # ['0', '1', '1']
        # ['01', '01', '10', '11', '10', '11']
        # ['011', '011', '101', '110', '101', '110']

        #list(set(perlist)):
        #['1', '0']
        #['11', '01', '10']
        #['101', '011', '110']

        #중복이 제거된 문자열 리스트 형태인 perlist에서 원소값 -> 정수형으로 바꾸고 소수 판별 함수에 적용
        for i in list(set(perlist)):
            if is_prime(int(i)): #소수일 경우 소수에 해당하는 값 answer 리스트에 담기
                answer.append(int(i))

    #중복된 값 제거한 채로, 리스트 안에 있는 값의 수 구하기
    answer = len(set(answer))

    return answer


print(solution("011"))