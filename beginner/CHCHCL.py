
ANS = []

T = int(input())

for l in range(T):
    N, M = map(int, input().split())
    if (N*M)%2:
        ANS.append('No')
    else:
        ANS.append('Yes')

for a in ANS:
    print(a)
