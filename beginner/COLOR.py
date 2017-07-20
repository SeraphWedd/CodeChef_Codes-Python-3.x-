
ANS = []

T = int(input())

for l in range(T):
    N = int(input())
    A = input()
    r = A.count('R')
    g = A.count('G')
    b = A.count('B')
    if r == 0:
        if g == 0 or b == 0:
            ANS.append(0)
        else:
            ANS.append(min(g, b))
    elif g == 0:
        if r == 0 or b == 0:
            ANS.append(0)
        else:
            ANS.append(min(r, b))
    elif b == 0:
        if r == 0 or g == 0:
            ANS.append(0)
        else:
            ANS.append(min(g, r))
    else:
        rgb = r + g + b
        ANS.append(rgb - max(r, g, b))

for a in ANS:
    print(a)
