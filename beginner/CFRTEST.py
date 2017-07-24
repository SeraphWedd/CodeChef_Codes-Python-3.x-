
get = lambda: map(int, input().split())

def frnd(a):
    cnt = 0
    temp = []
    for x in a:
        if x not in temp:
            temp.append(x)
            cnt += 1
    return cnt

ANS = []

T = int(input())

for l in range(T):
    n = int(input())
    D = get()
    ANS.append(frnd(D))

for a in ANS:
    print(a)
