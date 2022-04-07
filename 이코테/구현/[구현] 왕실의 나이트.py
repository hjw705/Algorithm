# 이코테-구현-왕실의 나이트
# 문제 설명 : 숫자로 된 행과 문자로 된 열을 입력받은 후, 해당 위치에서 나이트가 이동할 수 있는 경우의 수 출력
# 접근 방법 : 처음에 감을 잡지 못함- 아스키코드 숫자로 변환하는 법 ord('문자')
# 어려웠던 점 : 알파벳 문자로 입력받은 좌표값은 어떻게 해결해야 하는 지 감이 안왔었음
# => 문자열로 입력받고 열 부분 아스키코드로 처리
# 소문자 아스키 코드 -96 하면 열에 해당하는 10진수 값이 나옴 / 'A' 가 97임

n = input()
row = n[1]
column = int(ord(n[0])) - 96
cnt = 0 # 반환할 경우의 수

# 체스가 움직일 수 있는 경우의 수 8가지
moves = [(2,1),(2,-1),(-2,-1),(-2,1),(1,2),(1,-2), (-1,-2), (-1,2)]

for move in moves:
    next_row = row + moves[0]
    next_column =  column + moves[1]

    if next_row >= 1 and  next_row <= 8 and next_column >=1 and next_column <= 8:
        cnt += 1

print(cnt)