

ANS = []

T = int(input().strip(' '))

for l in range(T):
    N = int(input().strip(' '))
    if N < 1500:
        ANS.append(N<<1)
    else:
        ANS.append(float(N*1.98+500))

for a in ANS:
    print('%g' %a)
