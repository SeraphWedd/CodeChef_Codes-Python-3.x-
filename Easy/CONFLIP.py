
def counter(arr):
    i, n, q = arr
    if n%2 == 0:
        return n//2
    else:
        if i==q:
            return n//2
        else:
            return (n+1)//2
            

ANS = []

T = int(input())

for l in range(T):
    G = int(input())
    for _ in range(G):
        ANS.append(counter(map(int, input().split())))

for a in ANS:
    print(a)
