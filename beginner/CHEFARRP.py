
def counter(n, arr):
    total = 0
    cnt = 0
    mult = 1    

    for i in range(n):
        total += arr[i]
        mult *= arr[i]
        if total == mult:
            cnt += 1
            
    for start in range(1, n):
        total -= arr[start-1]
        mult //= arr[start-1]
        tmp_total = total
        tmp_mult = mult
        
        if tmp_total == tmp_mult:
            cnt += 1
            
        for end in range(n-1, start, -1):
            tmp_total -= arr[end]
            tmp_mult //= arr[end]
            
            if tmp_total == tmp_mult:
                cnt += 1
                    
    return cnt

ANS = []

T = int(input().strip(' '))

for i in range(T):
    N = int(input().strip(' '))
    ARR = list(map(int, input().strip(' ').split()))
    ANS.append(counter(N, ARR))
    
for a in ANS:
    print(a)
