

def vote(n, k, arr):
    total = 0
    for i in range(1, n+1):
        if arr[i-1] != i: #Didn't vote self
            count = arr.count(i)
            if count >= k: #qualified
                total += 1
    return total

    
ANS = []

T = int(input())

for l in range(T):
    N, K = map(int, input().split())
    ARR = list(map(int, input().split()))
    ANS.append(vote(N, K, ARR))

for a in ANS:
    print(a)
