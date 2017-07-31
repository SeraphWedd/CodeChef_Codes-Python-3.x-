
ANS = []

def coomilk(n, arr):
    if arr[-1] == 'cookie':
        return 'NO'
    for x in range(n-1):
        if arr[x] == 'cookie':
            if arr[x+1] == 'cookie':
                return 'NO'
    return 'YES'

T = int(input())

for l in range(T):
    N = int(input())
    A = list(input().split())
    ANS.append(coomilk(N, A))

for a in ANS:
    print(a)
