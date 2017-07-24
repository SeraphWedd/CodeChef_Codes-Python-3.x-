
def check(fl, arr):
    ans = []
    for a in fl:
        if a in arr:
            ans.append('YES')
        else:
            ans.append('NO')
    return ans

ANS = []

T = int(input())

for l in range(T):
    N, K = map(int, input().strip(' ').split())
    FL = input().split()
    ML = []
    for _ in range(K):
        ML += input().split()[1:]
    ANS.append(check(FL, ML))

for a in ANS:
    print(' '.join(a))
