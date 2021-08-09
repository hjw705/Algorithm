#level1_x만큼 간격이 있는 n개의 숫자

def solution(x, n):
    answer = []
    temp = x 
    answer.append(x)
    for i in range(n-1):
        temp += x # 기존 temp에  x만큼씩 더하기
        print(temp)
        answer.append(temp)
    return answer

# 간단한 풀이
# def number_generator(x, n):
#     # 함수를 완성하세요
#     return [i * x + x for i in range(n)]
# print(number_generator(2, 5))