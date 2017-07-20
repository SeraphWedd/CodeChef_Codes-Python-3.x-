

def evaluate(a, b, c):
    n = [x for x in a]
    for x in range(1, c):
        n[x] = a[x] - a[x-1]
    cnt = 0
    for i in range(c):
        if b[i] <= n[i]:
            cnt += 1
    return cnt
        
    
ANS = []

T = int(input())

for l in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ANS.append(evaluate(A, B, N))

for a in ANS:
    print(a)
