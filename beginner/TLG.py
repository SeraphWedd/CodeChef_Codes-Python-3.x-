
N = int(input())

W = []
L = []
P1 = 0
P2 = 0
for l in range(N):
    p1, p2 = [int(x) for x in input().split(' ')]
    P1 = P1 + p1
    P2 = P2 + p2
    d = P1 - P2
    if d > 0:
        W.append(1)
    else:
        W.append(2)
    L.append(abs(d))

ind = L.index(max(L))

print(W[ind], L[ind])
