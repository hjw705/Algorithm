# 백준 2609 - 최대공약수와 최소공배수
# 문제 설명: 두개의 자연수를 입력받아 최대 공약수 (greatest common division) 와 최소공배수 (least common multiple) 출력하기
# 해결 방법: 유클리드 호제법으로 처리 (최소공배수 공식 - 두 수의 곱 / 두 수의 최대공약수 )
#         (최대공약수 공식 - 큰수를 작은수로 나눈 후 나머지가 큰 수를 나누는 값이 되며, 나머지 값이 0이 될때까지 나눈다)
# 어려운 점: ide에서 살행할땐 문제가 없는데 자꾸 백준 테스트하면 틀림으로 나옴
# 보완할 점: 처음 gcd 코드짤 때 재귀쓰는데도 재귀의 장점을 부각하지 못하도록 코드 짬 - a>b , b<a 케이스 나눠서 코드 짬 -> 고치니깐 바로 됨 쩝

import sys
a, b = map(int,sys.stdin.readline().split())

def gcd(a,b): # 최대공약수 구하기
    if a % b == 0 :
        return b
    else:
        return gcd(b,a%b)

def lcm(a,b): # 최소공배수 구하기
    result = a * b // gcd(a,b)
    return result

print(gcd(a,b))
print(lcm(a,b))
