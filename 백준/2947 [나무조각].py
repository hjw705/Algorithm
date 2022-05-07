# 문제: 백준 2947 (나무조각) - 시뮬레이션
# 문제설명: 1-5가 적힌 번호의 나무조각이 무작위 순서로 입력 / 나무조각들을 첫번째 자리와 다음 자리,
# 그 다음 자리와 세번째 자리 등등으로 순서를 바꿔나감 / 조각의 위치가 바뀔때마다 조각의 순서 출력
# 풀이법: 버블 정렬로 바뀌는 위치 출력
# 느낀 점: 버블 정렬의 구현을 이제 잘 할 수 있게 되었다

import sys
num_list = list(map(int, sys.stdin.readline().split()))

# 끝까지 다 돌지 않아도 리스트의 최종 길이에서 1뺀 만큼만 돌아도 회전할때의 최종 위치값 구할 수 있으므로
for i in range(len(num_list)-1):
    # 1회전했을때 최종 위치를 제외한 나머지들만 비교해주면 됨
    for j in range(0, len(num_list)-i-1,1):
        # 첫번째 조각의 수가 두번째 조각의 수보다 크면 swap~ 이어서 리스트 끝까지 swap
        if num_list[j] > num_list[j+1]:
            num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
            # swap 될때마다 조각의 순서 출력
            for i in num_list:
                print(i, end=' ')
            print()