def gcf(x, y):
    large = max(x, y)
    small = min(x, y)
    r = 1
    while r:
        r = large%small
        if r != 0:
            large = small
            small = r
    return small

ANS = []

T = int(input().strip(' '))

for l in range(T):
    a, b = map(int, input().strip(' ').split())
    g = gcf(a, b)
    ANS.append((a//g)*(b//g))

for a in ANS:
    print(a)
    
