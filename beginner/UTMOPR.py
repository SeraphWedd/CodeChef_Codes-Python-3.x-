
def utm(arr, k):
    s = sum(arr)%2
    if k == 1:
        if s == 1:
            return 'even'
        else:
            return 'odd'
    else:
        return 'even'
        
get = lambda: map(int, input().split())

ANS = []

T = int(input())

for l in range(T):
    N, K = get()
    ARR = list(get())
    ANS.append(utm(ARR, K))

for a in ANS:
    print(a)
