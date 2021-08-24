# 그리디 (브론즈)_세탁소 사장 동혁
# 문제설명: 입력된 숫자를 0.25 (쿼터) / 0.10 (다임) / 0.05 (니켈) / 0.01 (페니) 로 나눠 최소한의 동전 개수로 거슬러주기
# 접근방법 : 최적의 해 == 최소한의 동전개수를 구하는 거 / 가장 큰 단위인 쿼터 단위로 먼저 나눠 주기
# 느낀 점 : 처음에 비효율적으로 1차원 리스트를 2차원 리스트로 바꿔주는거 생각했는데 바보같은 생각이었음 걍 바로바로 출력하면 됨

import sys
test_num = int(sys.stdin.readline())
test_case = [int(sys.stdin.readline().strip()) for i in range(test_num)]
coin_types = [25, 10, 5, 1]

for i in test_case:
    for coin in coin_types:
        print(i // coin, end=' ')
        i %= coin
    print()