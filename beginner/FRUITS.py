
ANS = []

T = int(input().strip(' '))

for l in range(T):
    N, M, K = map(int, input().strip(' ').split())
    d = abs(N - M)
    if d > K:
        ANS.append(d-K)
    elif K >= d:
        ANS.append(0)

for a in ANS:
    print(a)
