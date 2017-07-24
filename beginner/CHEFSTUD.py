
def evaluate(s):
    return s.count('<>')

ANS = []

T = int(input())

for l in range(T):
    ANS.append(evaluate(input()))

for a in ANS:
    print(a)
