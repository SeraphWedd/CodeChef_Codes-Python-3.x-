
def int_div(a, b, n):
    if n%2==1:
        a = a<<1
        return int(max(a, b)/min(a, b))
    else:
        return int(max(a, b)/min(a, b))
    

ANS = []
T = int(input())

for l in range(T):
    A, B, N = map(int, input().split())
    ANS.append(int_div(A, B, N))

for a in ANS:
    print(a)
