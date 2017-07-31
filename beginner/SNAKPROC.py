
def is_valid(s):
    snake = 0
    for c in s:
        if c == 'H':
            snake += 1
        elif c == 'T':
            snake -= 1
        if snake < 0 or snake > 1:
            return 'Invalid'
    if snake == 0:
        return 'Valid'
    else:
        return 'Invalid'

ANS = []

R = int(input())
for l in range(R):
    L = int(input())
    S = input()
    ANS.append(is_valid(S))

for a in ANS:
    print(a)
