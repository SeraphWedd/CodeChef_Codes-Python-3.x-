

ANS = []

T = int(input())

for l in range(T):
    S = input()
    if ('0' in S) and ('1' in S):
        if (S.count('0') == 1) or (S.count('1') == 1):
            ANS.append('Yes')
        else:
            ANS.append('No')
            
    elif len(S) == 1:
        ANS.append('Yes')
        
    else:
        ANS.append('No')

for a in ANS:
    print(a)
