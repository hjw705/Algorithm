#9093 단어뒤집기

import sys
input = sys.stdin.readline
answer=[]
n = int(input())

for i in range(n):
    result =' '.join([i[::-1] for i in input().split()])  # 공백 기준으로 문자열 거꾸로 join하기
    answer.append(result)


for i in answer:
    print(i)