
ANS = []

T = int(input())

for l in range(T):
    s = input()
    ANS.append(int(s[0]) + int(s[-1]))

for l in ANS:
    print(l)
    
