
def collision(n, m, arr):
    total = 0
    for g in range(m):
        cnt = 0
        for b in range(n):
            cnt += arr[b][g]
        total += (cnt)*(cnt-1)//2
    return total

ANS = []

T = int(input())

for l in range(T):
    N, M = map(int, input().split())
    ARR = []
    for _ in range(N):
        ARR.append(list(map(int, input())))
    ANS.append(collision(N, M, ARR))

for a in ANS:
    print(a)
