
def similar(a1, a2):
    cnt = 0
    for line in a1:
        if line in a2:
            cnt += 1
    if cnt >= 2:
        return 'similar'
    else:
        return 'dissimilar'
    
ANS = []

T = int(input())

for l in range(T):
    ARR1 = input().split()
    ARR2 = input().split()
    ANS.append(similar(ARR1, ARR2))

for a in ANS:
    print(a)
    
