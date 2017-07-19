

def comp(s1, s2):
    a1 = [x for x in s1]
    a2 = [x for x in s2]
    for i in range(len(a1)):
        c1 = a1[i]
        c2 = a2[i]
        if '?' not in [c1, c2]:
            if c1 != c2:
                return 'No'
    return 'Yes'

ANS = []

T = int(input().strip())

for l in range(T):
    str1 = input()
    str2 = input()
    ANS.append(comp(str1, str2))

for a in ANS:
    print(a)
