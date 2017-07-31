
def segm(s):
    start = False
    end = False
    for c in s:
        if c == '1':
            if end:
                return 'NO'
            if not start:
                start = True
                
        if c == '0':
            if start:
                end = True
    if not start:
        return 'NO'
    else:
        return 'YES'
        
ANS = []

T = int(input())

for l in range(T):
    S = input()
    ANS.append(segm(S))

for a in ANS:
    print(a)
