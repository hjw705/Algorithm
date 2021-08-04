#level1_최대공약수와 최소공배수
def solution(n, m):
    answer =[]
    #최대공약수
    for i in range(min(n,m), 0 , -1):
        if n%i==0 and m%i==0:
            answer.append(i)
            break

    #최소공배수
    for i in range(max(n,m), n*m+1):
        if i%n == 0 and i%m==0:
            answer.append(i)
            return answer

#더 간단한 코드
# def solution(n, m):
#     gcd = lambda a,b : b if not a%b else gcd(b, a%b)
#     lcm = lambda a,b : a*b//gcd(a,b)
#     return [gcd(n, m), lcm(n, m)]


