
ANS = []

def rect(arr):
    sides = []
    for s in arr:
        l = arr.count(s)//2
        if (l >= 1) and (s not in sides):
            for _ in range(l):
                sides.append(s)
    sides.sort()
    
    if len(sides) < 2:
        return -1
    else:
        return sides[-1]*sides[-2]
        
T = int(input())

for l in range(T):
    N = int(input())
    ARR = list(map(int, input().split()))
    ANS.append(rect(ARR))

for a in ANS:
    print(a)
