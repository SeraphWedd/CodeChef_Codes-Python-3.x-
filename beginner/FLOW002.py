T = int(input())
A = []
for l in range(T):
    A.append([int(x) for x in input().split(' ')])

for x, y in A:
    print(x%y)

