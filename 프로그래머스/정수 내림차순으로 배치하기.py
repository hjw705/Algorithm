# level 1_정수 내림차순으로 배치하기
def solution(n):
    listnum = []
    for i in range (len(str(n))):
        nam = n %10 #각각 정수의 자릿값에 해당하는 수
        n = n // 10
        listnum.append(nam) #자랏값에 해당하는 수 리스트에 넣기
    listnum.sort(reverse=True) #리스트 내림차순으로 정렬
    answer = list(map(str,listnum)) #str형 원소로 변환
    return int(''.join(answer)) #리스트 원소들 이어서 출력 -> Int 형으로 변환

#더 간단한 코드
# 입력받은 정수를 문자열로 만들어주고 리스트에 넣으면 각각 하나씩 리스트 원소값으로 들어감
# 이후 내림차순으로 정렬 가능함

# def solution(n):
#     ls = list(str(n))
#     ls.sort(reverse = True)
#     return int("".join(ls))