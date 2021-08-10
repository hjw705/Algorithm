#level1_문자열 내 마음대로 정렬하기
def solution(strings, n):
    new_lst = sorted(strings, key = lambda x: (x[n],x)) #n 번째 인덱스 기준으로 정렬 후, 단어의 사전순으로 정렬
    return new_lst
