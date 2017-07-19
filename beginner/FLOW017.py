
ANS = []

T = int(input())

for l in range(T):
    arr = list(map(int, input().strip(' ').split()))
    arr.sort()
    ANS.append(arr[-2])

for a in ANS:
    print(a)
