DENOM = [1, 2, 5, 10, 50, 100]

def count(n, d):
    if d == 0:
        return n
    else:
        x = DENOM[d]
        return (n//x) + (count(n%x, d-1))

ANS = []

T = int(input())

for l in range(T):
    N = int(input())
    ANS.append(count(N, 5))

for l in ANS:
    print(l)
    
