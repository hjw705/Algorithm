#level1_직사각형 별찍기
a, b = map(int, input().split(' '))
for i in range (b):
    for j in range(a):
        print("*", end='')
    print(' ')

#더 간단한 코드
# a, b = map(int, input().strip().split(' '))
# answer = ('*'*a +'\n')*b
# print(answer)