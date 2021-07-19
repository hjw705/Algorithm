#level1_두 정수 사이의 합
def solution(a, b):
  result = (abs(a-b) / 2) * (a+b) + (a+b)/2
  return int(result)
print(solution(2,-1))


#---더 간단한 코드----
# def adder(a, b):
#     if(a>b):
#         a,b = b,a
#     return sum(range(a,b+1))
# print( adder(3, 5))