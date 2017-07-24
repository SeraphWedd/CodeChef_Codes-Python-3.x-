
get = lambda: map(int, input().split())

def ave(n, k, arr):
    arr.sort()
    return sum(arr[k:n-k])/(n - 2*k)

ANS = []

T = int(input())

for l in range(T):
    N, K = get()
    ARR = list(get())
    ANS.append(ave(N, K, ARR))

for a in ANS:
    print('%f' %a)
