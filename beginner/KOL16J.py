
def legal(n, c):
    arr = [x+1 for x in range(n)]
    if arr == c:
        return 'no'
    
    c.sort()
    if arr == c:
        return 'yes'
    else:
        return 'no'
            
ANS = []

T = int(input())

for l in range(T):
    N = int(input())
    C = list(map(int, input().split()))
    ANS.append(legal(N, C))

for a in ANS:
    print(a)
