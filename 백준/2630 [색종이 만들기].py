# 문제: 색종이 만들기 (재귀)
# 문제 설명: 종이 한변의 길이 N 주어짐 / N * N 의 종이 분할하면서 1이나 0으로 만 이루어진 경우 종이수 +1
# 아닐 경우 계속 분해 / 0으로 칠해진 종이의 수와 1로 칠해진 종이 수 출력
# 풀이법: 좌표값 이용하기 / 첫번째 좌표는 0,0 으로 설정
import sys
n = int(sys.stdin.readline())
papers = [list(map(int,sys.stdin.readline().split())) for i in range (n)]
one_count = 0
zero_count = 0
def paper(x,y,n):
    global one_count, zero_count
    first_paper = papers[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if first_paper != papers[i][j]:
                next_paper = n // 2
                paper(x,y,next_paper)
                paper(x,y+n//2, next_paper)
                paper(x+n//2,y,next_paper)
                paper(x+n//2, y+n//2,next_paper)
                return
        if papers[x][y] == 1:
            one_count += 1
        elif papers[x][y] == 0:
            zero_count += 1
        return
paper(0,0,n)
print(zero_count)
print(one_count)