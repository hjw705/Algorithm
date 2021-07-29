#level1_평균구하기
def solution(arr):
   sum = 0
   for i in range(0,len(arr)):
       sum += arr[i]
       i += 1
       if i == len(arr):
           return sum / i

print(solution([1,2,3,4]))