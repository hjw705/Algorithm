seoul = []
def solution(seoul):

    if 'Kim' in seoul:
        answer = '김서방은 ' + str(seoul.index("Kim"))+ '에 있다'
        return answer

print(solution(seoul))