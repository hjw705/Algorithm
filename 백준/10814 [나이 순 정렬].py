#10814_나이순 정렬 (프로그래머스 문제 추가연습용)

import sys
n = int(sys.stdin.readline())
data = []
for i in range(n):
    age, name = map(str, sys.stdin.readline().split())
    age = int(age)
    data.append((age, name))

data.sort(key = lambda x:x[0])

for x,y in data:
    print(x,y)