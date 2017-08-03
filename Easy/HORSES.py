
ANS = []

T = int(input())

for l in range(T):
    N = int(input())
    ARR = list(map(int, input().split()))
    ARR.sort()
    for i in range(1, N):
        ARR[i-1] = ARR[i] - ARR[i-1]
    ANS.append(min(ARR))

for a in ANS:
    print(a)
