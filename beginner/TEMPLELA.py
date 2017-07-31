
def snake(n, h):
    if h[0] == h[-1] == 1:
        mxi = h.index(max(h))
        lp = h[:mxi]
        rp = h[mxi+1:][::-1]
        if lp == rp:
            for i in range(mxi):
                if h[i] != h[i+1] - 1:
                    return 'no'
            return 'yes'
        else:
            return 'no'
    else:
        return 'no'

ANS = []

S = int(input())

for l in range(S):
    N = int(input())
    H = list(map(int, input().split()))
    ANS.append(snake(N, H))

for a in ANS:
    print(a)
