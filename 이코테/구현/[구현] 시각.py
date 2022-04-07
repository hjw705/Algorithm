# 이코테-구현-시각
# 문제 설명 : 정수 N 입럭받기 / 00시 00분 00초 중에서 5가 들어가는 경우의 수 출력 (00시 ~23시 / 00분 ~ 59분 / 00초 ~59초)
# 접근 방법 : 문자열 비교로 5가 들어가 있을 경우 cnt +1 하기
# 어려웠던 점 : 문제를 처음에 잘못 이해함 / N시 까지의 시각을 범위안에서 경우의 수 따지는 걸로 해야 함

import sys
n = int(sys.stdin.readline())

cnt = 0
for i in range(n+1): # 시간
    for j in range(60): # 분
        for k in range(60): #초에 대한 경우의 수 안에서
            # 매 시각마다 h 가 포함되어 있을 경우 카운트 증가
            if str(n) in str(i) + str(j) + str(k):
                cnt += 1
print(cnt)