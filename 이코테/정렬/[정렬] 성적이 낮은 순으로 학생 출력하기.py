# 문제: 성적이 낮은 순으로 학생 출력하기 (이코테)
# 문제 설명: 이름과 성적 입력 받음 / 성적 낮은 순으로 학생 이름 출력하기
# 풀이법: 배열 원소의 [1] 값이 낮은 순으로 배열[0] 출력하기
# 느낀점: 흠,,
import sys
n = int(sys.stdin.readline())
student_list = []
for i in range(n):
    student_list.append(sys.stdin.readline().split())
student_list.sort(key=lambda student : int(student[1]))
for i in range(n):
    print(student_list[i][0], end= ' ')