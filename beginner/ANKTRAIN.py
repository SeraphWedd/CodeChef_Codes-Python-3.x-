
def partner(n):
    r = n%8
    if r == 3:
        return str(n+3)+'UB'
    elif r == 6:
        return str(n-3)+'UB'
    elif r == 2:
        return str(n+3)+'MB'
    elif r == 5:
        return str(n-3)+'MB'
    elif r == 1:
        return str(n+3)+'LB'
    elif r == 4:
        return str(n-3)+'LB'
    elif r == 7:
        return str(n+1)+'SU'
    elif r == 0:
        return str(n-1)+'SL'
ANS = []

T = int(input())

for l in range(T):
    N = int(input())
    ANS.append(partner(N))

for a in ANS:
    print(a)
