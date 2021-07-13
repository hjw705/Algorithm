# 팩토리얼 백준 10872번
def factorial_recursive(i):
    if i<=1: 
        return 1
    return i * factorial_recursive(i-1)

print(factorial_recursive(int(input())))