# 피보나치 수 5 백준 10870번
def fibo_recursive(i):
    if i==0:
        return 0
    if i ==1:
        return 1
    return fibo_recursive(i-1)+fibo_recursive(i-2)

print(fibo_recursive(int(input())))