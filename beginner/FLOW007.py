ANS = []

T = int(input().strip(' '))

for l in range(T):
    s = list(map(str, input().strip(' ')))
    s.reverse()
    ANS.append(''.join(s))
for a in ANS:
    print(int(a))
    
