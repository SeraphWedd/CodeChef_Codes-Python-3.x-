
ANS = []

T = int(input().strip(' '))

for l in range(T):
    a, b = map(int, input().strip(' ').split())
    total = 0
    for n in range(a, b+1):
        s = str(n)
        if s == s[::-1]: #compares original string and flipped string
            total += n
    ANS.append(total)

for a in ANS:
    print(a)
