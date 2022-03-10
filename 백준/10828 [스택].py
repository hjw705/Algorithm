# 백준 10828 - 스택
# 문제 설명: 스택의 기능 (push / pop / size / empty / top ) 구현
# 해결 방법: stack 클래스 생성 후, 배열 형식에서의 메소드들 활용하여 구현하기
# 어려운 점: 어렵지는 않은데 내가 어렵게 생각해서 어려워진 문제랄까
# 보완할 점: 로직은 맞는데 배열에 굳이 저장해서 출력하는 비효율적인 방식을 사용 / 그냥 바로 리스트화됨
# if 문으로만 하면 참 거짓 여부 상관없이 항상 실행하는 거니깐 낭비임

import sys

opNum = int(sys.stdin.readline()) # 명령의 수 입력받기
result = [] #출력값들 담을 리스트

for i in range(opNum): #명령어들 입력받기
    operation = sys.stdin.readline().split() #['push', '1'] 이런식으로 입력받게 됨

    if operation[0] == 'push':
        result.append(operation[1])

    elif operation[0] == 'pop':
        if len(result) == 0:
            print(-1)
        else:
            print(result.pop())

    elif operation[0] == 'top':
        if len(result) == 0:
            print(-1)
        else:
            print(result[-1])

    elif operation[0] == 'size':
        print(len(result))

    elif operation[0] == 'empty':
        if len(result) == 0:
            print(1)
        else:
            print(0)













