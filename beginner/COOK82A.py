
def wins(l):
    flag = 0
    if l['Barcelona'] > l['Eibar']:
        flag += 1
    if l['RealMadrid'] < l['Malaga']:
        flag += 1
        
    if flag == 2:
        return 'Barcelona'
    else:
        return 'RealMadrid'
    
ANS = []

T = int(input())

for l in range(T):
    lines = {}
    for _ in range(4):
        k, v = input().split()
        lines[k] = v
    ANS.append(wins(lines))

for a in ANS:
    print(a)
    
