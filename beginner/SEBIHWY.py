
ANS = []

T = int(input())

for l in range(T):
    S, SG, FG, D, TM = map(int, input().strip(' ').split())
    
    SPD = S + (D*180/TM)
    SE = abs(SPD - SG)
    FE = abs(SPD - FG)
    
    if SE < FE:
        ANS.append('SEBI')
    elif SE > FE:
        ANS.append('FATHER')
    elif SE == FE:
        ANS.append('DRAW')

for a in ANS:
    print(a)
