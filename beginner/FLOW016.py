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

def lcm(a, b, gcf):
    return (a*b)/gcf

ANS = []

T = int(input().strip(' '))

for l in range(T):
    a, b = map(int, input().strip(' ').split())
    g = int(gcf(a, b))
    l = int(lcm(a, b, g))
    ANS.append((g, l))

for g, l in ANS:
    print(g, l)
