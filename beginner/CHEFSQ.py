

ANS = []

T = int(input().strip(' '))

for l in range(T):
    N = int(input().strip(' '))
    ARR = list(map(int,input().strip(' ').split()))
    M = int(input().strip(' '))
    F = list(map(int,input().strip(' ').split()))
    
    count = 0
    for c in F:
        if c in ARR:
            count += 1
            
    if count == M:
        ANS.append('Yes')
    else:
        ANS.append('No')

for a in ANS:
    print(a)
