
global ls, ss

def legal(s):
    global ls, ss
    ls = list(s)
    ss = sorted(s)
    if ls == ss:
        return 'yes'
    else:
        return 'no'
    
                
ANS = []

T = int(input())

for l in range(T):
    S = input()
    ANS.append(legal(S))

for a in ANS:
    print(a)

