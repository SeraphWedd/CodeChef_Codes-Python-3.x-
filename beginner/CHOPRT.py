
def evaluate(a, b):
    if a > b:
        return '>'
    elif a < b:
        return '<'
    else:
        return '='

ANS = []

T = int(input().strip(' '))

for l in range(T):
    a, b = map(int, input().strip(' ').split())
    ANS.append(evaluate(a, b))

for a in ANS:
    print(a)
