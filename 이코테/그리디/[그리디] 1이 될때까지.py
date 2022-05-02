# 문제 : 1이 될때까지 (이코테 - 그리디)
# 문제설명: 어떠한 수가 1이 될때까지 해당 두 과정을 반복적으로 선택하여 수행
# 1) N에서 1 빼기 / 2) N을 K로 나누기
# 느낀점: 어떻게 하면 답지 같은 풀이를 생각하지..?

# 내가 짠 코드
# import sys
# n, k = map(int,sys.stdin.readline().split())
# count  = 0
# while n != 1:
#     if n%k == 0:
#         n = n //k
#         count +=1
#     else:
#         n = n -1
#         count += 1
#
#     if n == 1:
#         break
#
# print(count)

# 이코테 답지 (시간복잡도가 줄어드는 코드)
import sys
n, k = map(int,sys.stdin.readline().split())
count = 0

while True:
    # n이 k로 나누어 떨어지는 수가 될때까지 빼기
    target = (n//k) * k # k의 배수로 만들기
    count += (n-target) # k의 배수로 만들기까지의 -1 횟수 더하기
    n = target

    # n이 k보다 작을떼 ( 더이상 나눌 수 없을때) 반복문 탈출
    if n<k :
        break
    count += 1

    # k의 배수로 나눠주기
    n //= k

# n이 k보다 작아졌을때 계속 -1 해서 1로 만들기
count += (n-1)
print(count)