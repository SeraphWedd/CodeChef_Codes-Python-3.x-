from math import sqrt

def distance(a, b):
    x1, y1 = a
    x2, y2 = b
    return sqrt((x2-x1)**2 + (y2-y1)**2)

def in_range(a, b, c, r):
    d_ab = distance(a, b)
    d_bc = distance(b, c)
    d_ac = distance(a, c)

    if d_ab > r:
        if d_ac > r:
            return 'no'
        elif d_bc >r:
            return 'no'
        else:
            return 'yes'
    else:
        if d_bc > r:
            if d_ac > r:
                return 'no'
            else:
                return 'yes'
        else:
            return 'yes'

ANS = []

T = int(input())

for l in range(T):
    max_range = int(input().strip(' '))
    A = list(map(int, input().strip(' ').split()))
    B = list(map(int, input().strip(' ').split()))
    C = list(map(int, input().strip(' ').split()))

    ANS.append(in_range(A, B, C, max_range))

for l in ANS:
    print(l)
