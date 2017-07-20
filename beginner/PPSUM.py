
def SUM(N):
    return int((N/2)*(1+N))

def NSUM(D, N):
    c = N
    for x in range(D):
        c = SUM(c)
    return c

ANS = []

T = int(input().strip(' '))

for l in range(T):
    D, N = map(int, input().strip(' ').split())
    ANS.append(NSUM(D, N))

for a in ANS:
    print(a)
    
