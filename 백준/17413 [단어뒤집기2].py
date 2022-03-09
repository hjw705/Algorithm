# 백준 17413 - 단어 뒤집기 2
# 문제 설명 : 문자열 뒤집기
# 조건 : 태그 <> 안에 있는 문자열은 그대로 있고 태그 사이에 있는 문자열만 반대로 뒤집어서 출력한다
# 접근 방법 :
# 1) reverse 플래그로 반전 여부 판단
# 2) '<' 가 입력되면 반전 불필요하므로, reverse = False
# 3) '>'가 입력되면 반전이 필요할 수도 있으니간 reverse = True
# 4) reverse 의 초기값은 True로 설정하여 '<' 가 입력되지 않는다면 바로 반전되게 한다

# 정리) 문자열이 '<' '>' 빈스페이스, 반대로 출력해야 할 경우, 그냥 순회하는 문자열 출력해야 하는 경우 나누어서 처리

import sys
n = sys.stdin.readline().rstrip() # 예시: <open>tag<close> =>  <open>gat<close> 출력
answer = ''
word = ''
reverse = True #태그가 없을 경우를 위해 reverse 를 기본값으로 한다

for i in n: # 문자열 순회
    if i == '<': # '<' 로 태그가 시작하는 경우
        reverse = False # 태그 안은 문자열 반전 안하므로 reverse 가 false
        answer += word
        word = '<'

    elif i == '>': #'>' 가 있을 경우, 태그가 끝나는 거이므로
        reverse = True #이제 문자열 반대로 출력
        answer += (word + '>') # 출력해야 하는 문자열 + '>' 로 태그 마무리 하는 문자열
        word = '' # word 빈문자열로 초기화

    elif i == ' ': # 문자열 중 빈공간이 있을 경우
        answer += (word + ' ')
        word = ''

    elif reverse: # 반대로 출력해야 할 경우
        word = i + word

    else: # word에 문자열 순회하는 i 추가하며 문자열 만들어 나가기
        word += i

print(answer+word) #태그가 끝난 이후에 입력되는 문지열도 반대로 출력되어야 해서 word 더함







