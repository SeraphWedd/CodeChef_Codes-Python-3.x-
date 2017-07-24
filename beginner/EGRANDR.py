
def exam(n, arr):
    if 2 not in arr:
        if 5 in arr:
            ave = sum(arr)/n
            if ave >= 4:
                return 'Yes'
            else:
                return 'No'
    return 'No'

ANS = []

T = int(input())

for l in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    ANS.append(exam(N, A))

for a in ANS:
    print(a)
