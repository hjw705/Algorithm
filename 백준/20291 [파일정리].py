# 백준 20291 - 파일 정리
# 문제 설명 : 입력받을 파일들의 개수 입력하고 해당 파일을 입력하기,확장자의 이름와 해당 확정자 파일 개수를 출력하기
# 해결 방법: split('.') 뒤의 확장자 저장 / dictionary 의 key 형태로 저장 / 확장자 출력시 이름의 사전순 출력
# 어려운 점: 아직 딕셔너리 관련 메소드가 좀 덜 익숙한것

import sys
n = int(sys.stdin.readline()) #입력받을 파일의 수
extension = dict() #확장자들의 딕셔너리에 저장

for i in range(n):
    file = list(sys.stdin.readline().rstrip().split('.')) # , 기준으로 파일명, 확장자 분리 후, file 리스트에 저장
    extension[file[1]] = extension.get(file[1], 0) + 1 #해당 key 값이 없을 경우,두번째 인자 0으로, 그리고 그 인자에 +1 씩 더해서 확장자의 수 세어가기

file_list =[] # 딕셔너리의 key, value 값을 넣을 파일 리스트
for key in extension:
    file_list.append((key, extension.get(key)))

file_list.sort() # 파일 리스트 사전순으로 정렬

for word in file_list: #출력
    print(word[0], word[1])