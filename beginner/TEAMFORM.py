
ANS = []
T = int(input())

for l in range(T):
    N, M = map(int, input().split())
    UV = []
    for _ in range(M):
        UV.append(input())
    if N%2 == 0:
        ANS.append('yes')
    else:
        ANS.append('no')

for a in ANS:
    print(a)
