
def safehouse(a, x, y):
    safe = [i for i in range(1, 101)]
    d = x*y
    for w in a:
        lower = w-d - 1
        upper = w+d - 1
        if lower < 0:
            lower = 0
        if upper > 99:
            upper = 99
        for r in range(lower, upper + 1):
            safe[r] = 0
    return 100 - safe.count(0)
    
        

ANS = []

T = int(input().strip(' '))

for l in range(T):
    M, x, y = map(int, input().strip(' ').split())
    A = list(map(int, input().strip(' ').split()))
    ANS.append(safehouse(A, x, y))

for a in ANS:
    print(a)
