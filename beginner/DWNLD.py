
def compute(n, k, arr):
    t_time = 0
    t_price = 0
    for t, d in arr:
        if t_time + t > k:
            t_price += d*(t_time + t - k)
            t_time = k
        else:
            t_time += t
    return t_price

TC = int(input())

for l in range(TC):
    N, K = map(int, input().split())
    ARR = []
    for _ in range(N):
        ARR.append(list(map(int, input().split())))
    print(compute(N, K, ARR))
    
