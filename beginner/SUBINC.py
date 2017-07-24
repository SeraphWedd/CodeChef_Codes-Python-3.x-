
def count(a, n):
    b = [1 for x in range(n)]
    for c in range(1, n):
        if a[c-1] <= a[c]:
            b[c] = b[c-1] + 1
        elif a[c-1]>a[c]:
            b[c] = 1
            
    return sum(b)
    
ANS = []

T = int(input())

for l in range(T):
    N = int(input())
    ARR = list(map(int, input().strip(' ').split()))
    ANS.append(count(ARR, N))

for a in ANS:
    print(a)
