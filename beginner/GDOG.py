

def max_bark(n, k):
    mx = 1
    for x in range(2, k+1):
        mx = max(mx, n%x)
    return mx

ANS = []

T = int(input().strip(' '))

for l in range(T):
    a, b = map(int, input().strip(' ').split())
    ANS.append(max_bark(a, b))

for c in ANS:
    print(c)
    
