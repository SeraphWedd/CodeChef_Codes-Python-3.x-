import itertools

def is_enough(n, m, arr):
    #Remove notes with value higher than m
    arr.sort()
    for i in range(n):
        if arr[i] > m:
            arr = arr[:i]
            n = len(arr)
            break
    
    for i in range(1, n+1):
        #find the set of i length tuples from banknotes
        all_combinations = list(itertools.combinations(arr, i))
        
        # find the sum of each set
        if m in [sum(ls) for ls in all_combinations]:
            return "Yes"
    return "No"

ANS = []
T = int(input())

for l in range(T):
    N, M = map(int, input().split())
    ARR = []
    for _ in range(N):
        ARR.append(int(input()))
    ANS.append(is_enough(N, M, ARR))

for a in ANS:
    print(a)
