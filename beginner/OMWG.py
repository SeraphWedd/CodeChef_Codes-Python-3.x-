

def maxi(n, m):
    return n*(m-1) + m*(n-1)
ANS = []

T = int(input())

for l in range(T):
    N, M = map(int, input().split())
    ANS.append(maxi(N, M))

for a in ANS:
    print(a)
