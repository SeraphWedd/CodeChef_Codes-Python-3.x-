
ANS = []

T = int(input().strip(' '))

for l in range(T):
    N = int(input().strip(' '))
    ARR = list(map(int, input().strip(' ').split()))
    ANS.append(min(ARR)*(N-1))

for a in ANS:
    print(a)
    
