
def trisq(b):
    if b < 4:
        return 0
    else:
        a = (b-2)//2
        return int((a/2)*(1 + a))

ANS = []

T = int(input().strip(' '))

for l in range(T):
    ANS.append(trisq(int(input().strip(' '))))

for a in ANS:
    print(a)
    
