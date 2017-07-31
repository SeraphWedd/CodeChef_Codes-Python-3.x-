
get = lambda: map(int, input().split())

def count(a, b, c, d):
    cnt = 0
    for x in range(a, min(b+1, d+1)):
        cnt += d - max(c, x+1) + 1
    return cnt

ANS = []

T = int(input())

for l in range(T):
    a, b, c, d = get()
    ANS.append(count(a, b, c, d))

for a in ANS:
    print(a)
    
