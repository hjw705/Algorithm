# level1_모의고사
# 문제 설명: 정답배열에 해당하는 값들에 따른 수포자1,2,3 중 고득점자
# 접근 방법: 1)  수포자의 주기의 길이가 다르므로 5,8,10 으로 나눈 나머지와 비교를 해야 함
# 2) max 함수 사용 +  반환하는 최종리스트에 수포자들의 sum 값 넣은 리스트의 인덱스값+1 을 넣어 수포자 번호 반환

def solution(answers):
    student1 = [1, 2, 3, 4, 5]
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    sum = [0,0,0] # 각 수포자들이 정답 리스트의 요소들과 비교를 한 후, 같을 경우 sum이 +1 되는 부분 초기화
    answer = [] # 최종 반환할 리스트 초기화

    # 정답 리스트와 비교하여 각각의 수포자들 주기에 따른 value 값 비교
    for key, value in enumerate(answers):
        if value == student1 [key % 5]:
            sum[0] += 1
        if value == student2 [key % 8]:
            sum[1] += 1
        if value == student3 [key % 10]:
            sum[2] += 1

    # 3명의 수포자들의 sum 값 담는 리스트, 'result'
    result = [sum[0], sum[1], sum[2]]

    # 최댓값의 result 리스트와 result 의 값이 같을 경우, 반환 리스트 처리
    for key, value in enumerate(result):
        if value == max(result):
            answer.append(key+1)
    return answer








