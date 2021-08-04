A = int(input())
B = int(input())
C = int(input())

answer = A * B * C
answer = str(answer)
list_answer = list(answer) #문자열 -> 문자 하나씩 분해하기

for i in range(0,10): #1-9까지 숫자 몇번 쓰였는지 출력
    print(answer.count(str(i)))