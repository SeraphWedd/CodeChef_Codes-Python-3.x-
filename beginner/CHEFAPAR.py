
def rent(n, a):
    total = 0
    late = a.count(0)
    if late > 0:
        st = a.index(0)
        pd = a[st:].count(1)
        total = 1100*late + pd*100
    return total
            

ANS = []
T = int(input())

for l in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    ANS.append(rent(N, A))

for a in ANS:
    print(a)
