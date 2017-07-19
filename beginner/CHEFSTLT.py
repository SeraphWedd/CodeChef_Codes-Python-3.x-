
def comp(s1, s2):
    mx = 0
    mn = 0
    a1 = [x for x in s1]
    a2 = [x for x in s2]
    for i in range(len(a1)):
        c1 = a1[i]
        c2 = a2[i]
        if '?' not in [c1, c2]:
            if c1 != c2:
                mn += 1
                mx += 1
        elif '?' in [c1, c2]:
            mx += 1
    return mn, mx

ANS = []

T = int(input().strip(' '))

for l in range(T):
    str1 = input()
    str2 = input()
    ANS.append((comp(str1, str2)))

for a, b in ANS:
    print(a, b)
