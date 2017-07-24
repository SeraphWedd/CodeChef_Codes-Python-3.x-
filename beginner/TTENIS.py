
def win(s):
    o = s.count('1')
    z = s.count('0')
    if o > z:
        return 'WIN'
    else:
        return 'LOSE'

ANS = []

T = int(input())

for l in range(T):
    ANS.append(win(input()))

for a in ANS:
    print(a)
