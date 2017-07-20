from math import sqrt
def maxheight(n):
    x = (-1 + sqrt(1 + 8*n))/2
    return int(x)
    
ANS = []

T = int(input().strip(' '))

for l in range(T):
    N = int(input().strip(' '))
    ANS.append(maxheight(N))

for a in ANS:
    print(a)
