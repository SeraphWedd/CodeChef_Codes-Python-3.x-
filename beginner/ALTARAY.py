
def subarray(n, a):
    ans = []
    cnt = 1
    for x in range(1, n):
        if a[x] * a[x-1] > 0:
            for i in range(cnt, 0, -1):
                ans.append(str(i))
            cnt = 1
        else:
            cnt += 1
    for i in range(cnt, 0, -1):
        ans.append(str(i))
    return ans

ANS = []

T = int(input())

for l in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    ANS.append(subarray(N, A))

for a in ANS:
    print(' '.join(a))
