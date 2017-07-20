

def evaluate(l, r, n):
    temp = [0 for x in l]
    for i in range(n):
        temp[i] = l[i]*r[i]
    mx = max(temp)
    if temp.count(mx) == 1:
        return temp.index(mx) + 1
    else:
        ind = []
        for i in range(n):
            if temp[i] == mx:
                ind.append(i)
        curr = 0
        ans = 0
        for i in ind:
            if curr < r[i]:
                ans = i
                curr = r[i]
        return ans + 1
        

ANS = []

T = int(input())

for l in range(T):
    N = int(input())
    L = list(map(int, input().split()))
    R = list(map(int, input().split()))
    ANS.append(evaluate(L, R, N))

for a in ANS:
    print(a)
    
