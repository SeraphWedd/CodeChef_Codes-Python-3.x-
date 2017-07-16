ANS = []
T = int(input())

for l in range(T):
    A, B = map(int, input().split(' '))
    ANS.append([max([A, B]), A+B])

for a, b in ANS:
    print(a, b)
