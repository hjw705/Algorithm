#level1_k번째수
# 문제설명 : 배열의 i 번째부터 j번째 숫자까지 자르고 정렬한 후 k 번째에 있는 수 구하기
# 접근방법: 1) commands 배열의 i ~ j번째에 해당하는 배열 추출 / 2) 해당 배열 정렬 / 3) j번째 원소 구하고 리스트에 넣기
# 지난번에 한번에 안풀려서 짜증났는데 오늘은 한번에 풀려서 기분 쨰짐

def solution(array, commands):
    new_array = []
    answer = []
    for i in range(0,len(commands)):
        new_array.append(sorted(array[(commands[i][0])-1 : (commands[i][1])]))
        index = commands[i][2]
        answer.append(new_array[i][index-1])
    return answer
print(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))