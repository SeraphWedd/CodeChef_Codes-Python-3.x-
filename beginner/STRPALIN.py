
get = lambda: map(int, input().split())

def palinstr(a, b):
    for c in a:
        if c in b:
            return 'Yes'
    return 'No'
    
ANS = []

T = int(input())

for l in range(T):
    A = list(input())
    B = list(input())
    ANS.append(palinstr(A, B))

for a in ANS:
    print(a)
