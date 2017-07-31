

def nothingcom(n, m, a, b):
    dic = {}
    for i in range(n):
        try:
            dic[a[i]] += 1
        except KeyError:
            dic[a[i]] = 0

    for i in range(m):
        try:
            dic[b[i]] += 1
        except KeyError:
            dic[b[i]] = 0
    return sum(dic.values())

ANS = []
T = int(input())
for l in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ANS.append(nothingcom(N, M, A, B))

for a in ANS:
    print(a)
