

ANS = []

T = int(input())

for l in range(T):
    N = int(input())
    ARR = list(map(int, input().split()))
    K = ARR[int(input())-1]
    ARR.sort()
    ANS.append(ARR.index(K)+1)

for a in ANS:
    print(a)    
