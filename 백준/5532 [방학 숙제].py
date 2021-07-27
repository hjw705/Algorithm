import math
L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

l=math.ceil(A/C)
m=math.ceil(B/D)
study_days=max(l,m)
print(L-study_days)