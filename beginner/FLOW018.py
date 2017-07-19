
def factorial(N):
    if N == 0:
        return 1
    else:
        return N*factorial(N-1)

ANS = []

T = int(input())

for l in range(T):
    N = int(input().strip(' '))
    ANS.append(factorial(N))

for a in ANS:
    print(a)
