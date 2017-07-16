def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

T = int(input())
for l in range(T):
    print(factorial(int(input())))
    
