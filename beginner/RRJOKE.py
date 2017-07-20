
def path(arr):
    temp = [x for x in arr]
    temp.sort()
    p = 0
    for a in temp:
        p ^= (arr.index(a)+1)
    return p

ANS = []

T = int(input().strip(' '))

for l in range(T):
    N = int(input().strip(' '))
    ARR = [0 for x in range(N)]
    for x in range(N):
        ARR[x] = tuple(map(int, input().strip(' ').split()))
    ANS.append(path(ARR))

for a in ANS:
    print(a)
