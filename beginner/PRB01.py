
def is_prime(n):
    if n in (1, 2):
        return 'yes'
    
    if n%2 == 0:
        return 'no'
    
    for x in range(3,(n+1)//2+1, 2):
        if n%x == 0:
            return 'no'

    return 'yes'

ANS = []

T = int(input().strip(' '))

for l in range(T):
    ANS.append(is_prime(int(input().strip(' '))))

for l in ANS:
    print(l)
    
