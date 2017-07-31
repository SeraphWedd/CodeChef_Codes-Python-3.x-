
ANS = []

T = int(input())

for l in range(T):
    N, P = input().split()
    A = list(map(int, input().split()))
    if N=='1' and A[0]%2==0 and P=='Dee':
        ANS.append('Dee')
    else:
        ANS.append('Dum')

for a in ANS:
    print(a)
