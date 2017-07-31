
def factors(n, m, c):
    cnt = 0
    for x in range(1, c+1):
        if x > n:
            break
        else:
            if c%x == 0:
                if c/x <= m:
                    cnt += 1
    return cnt
              

ANS = []

T = int(input())

for l in range(T):
    N, M, C = map(int, input().split())
    ANS.append(factors(N, M, C))
    
for a in ANS:
    print(a)
