#실버 5_단어 정렬 (프로그래머스 문제 추가연습용)

num = int(input()) #입력받을 숫자의 갯수
temp =[]
for i in range(num):
    temp.append(input()) #빈 리스트에 입력한 숫자들 넣기
temp.sort(key = lambda x:(len(x),x)) #(1) 리스트의 길이, (2)사전순으로 정렬

answer =[]
#리스트 중복 제거
for value in temp:
    if value not in answer:
        answer.append(value)

#리스트에서 원소값들 추출
for i in answer:
    print(i)
