# 프로그래머스 - 완주하지 못한 선수
# 문제 설명: 마라톤에 참여한 참가자들의 이름을 담은 배열과 완주한 선수들의 이름을 담은 배열이 주어질 때, 완주하지 못한 선수들의 이름 return 하기
# 해결 방법: 리턴할 정답을 딕셔너리 형태로 설정 / 각각의 참가자 배열과 완주 배열을 딕셔너리 안에 넣기 / get 함수 써서 각각의 키값에 해당하는 value값을 추가하고,
#   중복되는 값들을 처리하기 위해 value 를 활용함
# 어려운 점: 문제 미완 -> 해설 보고 참조
# 보완할 점: 해쉬를 무조건 다 사용해야 한다는 생각에 핵심적인 부분에서 해쉬 쓰는 것을 놓침

def solution(participant, completion):
    answer = {}

    # participant = ['a','b','b'] 일 경우
    # answer = {'a' : 1, 'b':2..}
    for i in participant:
        answer[i] = answer.get(i,0) + 1 # dict.get(key,value) - 딕셔너리에서 찾을 키

    # completion 에 포함된 이름의 key의 value -1 하기
    for j in completion:
        answer[j] -= 1

    # pariticpant 에는 있지만 completion 에 없는 이름만 value가 1로 남으므로 그것을 리턴
    for k in answer:
        if answer[k] : return k