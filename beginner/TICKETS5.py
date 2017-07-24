
def success(s):
    chars = []
    
    for c in s:  
        if (c not in chars) and (len(chars) < 2):
            chars.append(c)
        elif len(chars) == 2:
            break
        
    for c in range(1, len(s)):
        if s[c] == s[c-1]:
            return 'NO'
        elif s[c] not in chars:
            return 'NO'
    return 'YES'

ANS = []

T = int(input())

for l in range(T):
    ANS.append(success(input().strip(' ')))

for a in ANS:
    print(a)
