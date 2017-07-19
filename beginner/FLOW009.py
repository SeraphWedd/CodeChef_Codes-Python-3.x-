
def evaluate(q, p):
    total = q*p
    if q >= 1000:
        return total*0.9
    else:
        return total

ANS = []

T = int(input().strip(' '))

for l in range(T):
    a, b = map(int, input().strip(' ').split())
    ANS.append(evaluate(a, b))
for a in ANS:
    print('%.6f' %a)
    
