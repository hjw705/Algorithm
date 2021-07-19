#level1_자연수 뒤집어 배열로 만들기
def solution(n):
  answer = []
  for i in range(len(str(n))):
    nam = n%10
    n = n // 10
    answer.append(nam)
  return answer

#더 간단한 풀이
# def digit_reverse(n):
#     return list(map(int, reversed(str(n))))