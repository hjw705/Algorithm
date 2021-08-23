# level1_체육복
# 문제설명: 인접해있는 인덱스의 학생들끼리 체육복을 빌려줄 수 있다.
# 총 인원수(N) 와 도난 당한 학생들(Lost)과 빌린 학생들(Reserve)의 배열을 참고하여,체육복을 빌려주고 최대한으로 많이 빌려줄 수 있는 학생 수 반환하기
# 주의사항: 1) 중복이 없다 => Lost 배열과 Reserve 내의 원소값이 unique
#        ex) lost = [1,1,2] reserve [3,3,5,4,2]

#        2) 여벌의 체육복 있는 학생도 도난 당했을 수 있음
#        ex) lost = [1,2,3] reserve [3,4,5]

# 접근방법 : 도난당한 학생들과 빌려주는 학생들에 대한 중복 제거 -> 도난 당한 학생을 양쪽의 학생이 도와줄 수 있는 경우,왼쪽에 있는 학생부터 빌려주기
# 코드 설명 : n=5 / lost = [2,4] / reserve = [1,3,5] 일 경우, 양쪽에서 2, 4는 양쪽에서 도와줄 수 있다
#          n=5 / lost = [2,4] / reserve = [3,5] 일 경우, 양쪽에서 3을 기준으로 4번부터 도와주면 2번은 도움을 못받음. 따라서 왼쪽부터 탐색
# 느낀 점 : 문제를 풀때 주어진 테스트케이스만 생각을 해서 문제를 어떻게 풀어나가야 할지 감이 오지 않았는데 위와 같은 테스트 케이스를 통해 어떤 요소부터
#         탐색해 나가야 할지 깨닫게 됨 / 앞으로 다른 문제들 풀떄도 이런 테스트케이스를 직접 만들어서 생각해봐야겠음

def solution(n, lost, reserve):
    # 주의사항 2가지에 해당하는 중복 제거
    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)

    #reserve 의 i-1 요소, 즉 왼쪽 학생부터 탐색하고 만약 없다면 오른쪽 탐샏
    # 예시 ) n=5 / lost = [2,4] / reserve = [1,3,5]
    for i in set_reserve:
        if i-1 in set_lost: # 5-1 = 4 in set_lost
            set_lost.remove(i-1) # 4 없애기

        elif i+1 in set_lost: # 2 in set_lost
            set_lost.remove(i+1) # 2 없애기
    return n-len(set_lost) # 5 반환

print(solution(5, [2,4], [1,3,5]))