
get = lambda: map(int, input().split())

def evals(ca, ss, k, m):
    sm = []
    for arr in ca:
        sm.append(sum(arr))
    sm.sort()
    p = sum(ss)
    l = sm[-k]
    d = l - p + 1
    if d > m:
        return 'Impossible'
    else:
        return max(0, d)

ANS = []

T = int(input())

for l in range(T):
    N, K, E, M = get()
    AE = []
    for _ in range(N-1):
        AE.append(get())
    SS = list(get())
    ANS.append(evals(AE, SS, K, M))

for a in ANS:
    print(a)
