
def balance(arr, k):
    total = 0
    for x in arr:
        a = x%k
        if x < k:
            total += (k-a)
        else:
            total += min(a, k-a)
    return total

ANS = []

T = int(input().strip(' '))

for l in range(T):
    N, K = map(int, input().strip(' ').split())
    ARR = map(int, input().strip(' ').split())
    ANS.append(balance(ARR, K))

for a in ANS:
    print(a)
