
get = lambda: map(int, input().split())

def lazy(n, b, m):
    if n == 1:
        return m
    elif n%2 == 0:
        return m*(n//2) + b + lazy(n//2, b, m<<1)
    else:
        return m*(n+1)//2 + b + lazy(n//2, b, m<<1)
    
ANS = []

T = int(input())

for l in range(T):
    N, B, M = get()
    ANS.append(lazy(N, B, M))

for a in ANS:
    print(a)
