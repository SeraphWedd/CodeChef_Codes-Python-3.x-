
def count(a, b, n):
    bothti = 0
    bothuu = 0
    for x in range(1, n+1):
        if (x in a) and (x in b):
            bothti += 1
        elif (x not in a) and (x not in b):
            bothuu += 1
    return bothti, bothuu

ANS = []

T = int(input().strip(' '))

for l in range(T):
    N, M, K = map(int, input().strip(' ').split())
    A = list(map(int, input().strip(' ').split()))
    B = list(map(int, input().strip(' ').split()))
    ANS.append((count(A, B, N)))

for a,b in ANS:
    print(a, b)
