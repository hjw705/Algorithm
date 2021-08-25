# level1_하샤드 수
# 문제설명: X의 자릿수 합으로 X가 나누어져야 함
# 접근방법 : X를 자리수별로 나눠주고 그 합 구하기 -> 합으로 X 나누고 나눠떨어지면 true 아니면 false return
# 느낀 점 : 리스트 map 해서 리스트 형태 아예 바꾸는 거 더 익숙해져야 함 / 쉬운 문제였음

def solution(x):
    num_list = list(map(int,str(x))) #입력받은 정수를 문자열 변환 후 리스트로 각각의 자릿수를 믄지열 리스트로 변환해줌
                                    # -> map 해서 int 형 리스트로 변환
    sum_num = 0
    for i in num_list: # 자릿수 리스트 안에 있는 요소들 더하기 (sum_num)
        sum_num += i

    if (x % sum_num == 0): # 입력받은 수 x가 sum_num 으로 나누어 떨어질 경우 true 반환 , 아니면 false
        return True
    else:
        return False