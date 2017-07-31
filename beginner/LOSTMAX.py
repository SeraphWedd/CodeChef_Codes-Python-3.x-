
ANS = []
T = int(input())

for l in range(T):
    ARR = list(map(int, input().split()))
    ARR.remove(len(ARR)-1)
    ANS.append(max(ARR))

for a in ANS:
    print(a)
