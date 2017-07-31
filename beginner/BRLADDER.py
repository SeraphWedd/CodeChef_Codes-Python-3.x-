
get = lambda: map(int, input().split())

ANS = []

Q = int(input())

for l in range(Q):
    a, b = get()
    if abs(a - b) == 2:
        ANS.append('YES')
    elif min(a, b)%2 == 1 and abs(a - b) == 1:
        ANS.append('YES')
    else:
        ANS.append('NO')
for a in ANS:
    print(a)
