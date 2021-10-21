# level1_키패드 누르기
# < 문제 설명 >
# 0) 처음 왼쪽은 "*", 오른쪽 손가락은 '#' 에 초기화
# 1) 왼쪽 손가락 움직이는 경우: (1,4,7) / 오른쪽 손가락 움직이는 경우: (3,6,9)
# 2) 가운데 번호인 경우, (2,5,8,0) -> 두 엄지손가락의 현재 키패드의 위치에서 더 가까운 엄지손가락
#  만약 거리가 같다면, 오른손잡이인지, 왼손잡이인지에 따라 결정

# 접근 방법: 거리 구하는 distance 함수를 따로 구현, 맨하튼 거리 공식 사용

def solution(numbers, hand):
    # 처음 키패드에 놓여져 있는 거 초기화
    left_s= '*'
    right_s= '#'
    answer = ''

    # 입력받은 리스트 순회
    for n in numbers:
        if n in [1,4,7]:
            answer += 'L'
        elif n in [3,6,9]:
            answer += 'R'

        # 2,5,8,0 에 있을 경우 distance 구하기  (현재 위치한 자리, 입력받은 자리) 간에
        elif n in [2,5,8,0]:
            d_r = distance(left_s, n)
            d_l = distance(right_s, n)

            if d_r > d_l:
                answer += 'L'

            elif d_r < d_l:
                answer += 'R'

            # 거리가 같을 경우 (왼쪽, 오른쪽) -> hand 로 구분하기
            elif d_r == d_l:
                if hand =='right':
                    answer += 'R'
                    right_s = n
                else:
                    answer +='L'
                    left_s = n
    return answer

# 손의 위치와 입력받은 숫자간의 거리 구하기

def distance(hand, number):
    # 딕셔너리 튜플 값으로  키패드의 좌표 정리 (문자열, 튜플) 로
    location ={'1': (0,0), '2': (0,1), '3': (0,2),
               '4': (1,0), '5':(1,1), '6': (1,2),
               '7': (2,0), '8': (2,1), '9': (2,2),
               '*': (3,0), '0':(3,1), '#': (3,2)}

    hand = str(hand)
    number = str(number)
    x_h, y_h = location[hand] # 튜플에서 해당 키값의 좌표 튜플 구하기
    x_n, y_n = location[number]
    # 맨하튼 거리 공식 사용
    return abs(x_h-x_n) + abs(y_h - y_n)


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))








