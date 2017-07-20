
ANS = []

T = int(input().strip(' '))

for l in range(T):
    s = input()
    ANS.append(min(s.count('a'), s.count('b')))

for a in ANS:
    print(a)
