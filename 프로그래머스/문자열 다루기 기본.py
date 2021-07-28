#level1_문자열 다루기
def solution(s):
    if len(s) ==4 or len(s)==6:
        if s.isdigit(): #isdigit() : 문자열이 전부 숫자로 이루어져 있는지
            return bool(1)
        else:
            return bool(0)
    else: return bool(0)