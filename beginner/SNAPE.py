from math import sqrt
ANS= []

def compute(b, ls):
    rs = []
    #rs is straight
    rs.append(sqrt(ls**2 - b**2))
    #ls is straigh
    rs.append(sqrt(ls**2 + b**2))
    ANS.append(rs)

T = int(input())

for l in range(T):
    B, LS = [int(x) for x in input().split(' ')]
    compute(B, LS)

for s, l in ANS:
    print('%.5f %.5f' %(s, l))
