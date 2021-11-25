#level1_최대공약수와 최소공배수
def gcd(n1,n2):
    if n1 < n2: 
        if n2 % n1 == 0:
            return n1
        else:
          return gcd(n1, int(n2%n1))
    else:
        if n1 % n2 == 0:
            return n2
        else:
          return gcd(n2, int(n1%n2))

def solution(n, m):
    gcd(n,m)
    answer = [gcd(n,m), int(n*m / gcd(n,m))]
    return answer

#더 간단한 코드
# def solution(n, m):
#     gcd = lambda a,b : b if not a%b else gcd(b, a%b)
#     lcm = lambda a,b : a*b//gcd(a,b)
#     return [gcd(n, m), lcm(n, m)]


