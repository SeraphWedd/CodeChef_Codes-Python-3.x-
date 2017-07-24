
def dev(arr, t):
    mn = arr[0]
    mx = arr[-1]
    if t >= mn and t <= mx:
        return 'Yes'
    else:
        return 'No'

N, Q = map(int, input().split())
ARR = list(map(int, input().split()))
ARR.sort()

for l in range(Q):
    print(dev(ARR, int(input())))
