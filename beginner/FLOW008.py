
ANS = []

T = int(input())

for l in range(T):
    if int(input()) < 10:
        ANS.append('What an obedient servant you are!')
    else:
        ANS.append(-1)

for l in ANS:
    print(l)
    
