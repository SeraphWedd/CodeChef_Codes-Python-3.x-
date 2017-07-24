

get = lambda: map(int, input().split())
ANS = []

T = int(input())

for l in range(T):
    x1, y1, x2, y2 = get()
    if x1 == x2:
        if y1 < y2:
            ANS.append('up')
        elif y1 > y2:
            ANS.append('down')
    elif y1 == y2:
        if x1 < x2:
            ANS.append('right')
        elif x1 > x2:
            ANS.append('left')
    else:
        ANS.append('sad')

for a in ANS:
    print(a)
