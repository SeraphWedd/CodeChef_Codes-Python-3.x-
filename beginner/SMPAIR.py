

ANS = []

T = int(input())

for l in range(T):
    L = int(input().strip(' '))
    ARR = list(map(int, input().strip(' ').split()))
    x = min(ARR)
    ARR.remove(x)
    y = min(ARR)
    ANS.append(x+y)

for l in ANS:
    print(l)
