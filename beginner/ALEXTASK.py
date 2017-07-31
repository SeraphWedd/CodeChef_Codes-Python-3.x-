
def gcf(x, y):
    large = max(x, y)
    small = min(x, y)
    r = large%small
    while r:
        r = large%small
        if r != 0:
            large, small = small, r
    return small

def lcm(a, b):
    return (a*b)//gcf(a, b)

def timer(n, arr):
    lcmList = []
    for a in range(1, n):
        temp = []
        for b in range(a):
            temp.append(lcm(arr[a], arr[b]))
        lcmList.append(min(temp))
    return min(lcmList)

ANS = []
T = int(input())

for l in range(T):
    N = int(input())
    ARR = list(map(int, input().split()))
    ARR.sort()
    ANS.append(timer(N, ARR))

for a in ANS:
    print(a)
