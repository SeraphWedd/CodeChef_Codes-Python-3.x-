
def good(n):
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 2]
    else:
        ans = [1]
        for x in range(1, n):
            ans.append((x<<1) + 1)
        return ans
    
ANS = []

T = int(input())

for l in range(T):
    N = int(input())
    ANS.append(good(N))

for a in ANS:
    print(' '.join(map(str, a)))
