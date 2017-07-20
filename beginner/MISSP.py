
ANS = []

T = int(input().strip(' '))

for l in range(T):
    acc = 0
    for _ in range(int(input().strip(' '))):
        acc ^= int(input().strip(' '))
    ANS.append(acc)

for a in ANS:
    print(a)
