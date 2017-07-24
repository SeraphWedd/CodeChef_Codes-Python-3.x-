
get = lambda: map(int, input().strip(' ').split())

def minmax(c, d, l):
    mn = 0
    mx = (c+d)*4
    
    t = c - (2*d)
    if c <= d*2:
        mn = d*4
        
    else:
        mn = (d+t)*4
    
    if l >= mn and l <= mx and l%4 == 0:
        return 'yes'
    
    else:
        return 'no'

ANS = []

T = int(input())

for l in range(T):
    C, D, L = get()
    ANS.append(minmax(C, D, L))

for a in ANS:
    print(a)
    
