
get = lambda: map(int, input().split())

def winnings(n, cor, ans, arr):
    cnt = 1
    for i in range(n):
        if cor[i] == ans[i]:
            cnt += 1
            
    if cnt == n + 1:
        return arr[n]
    
    return max(arr[:cnt])

ANS = []

T = int(input())

for l in range(T):
    N = int(input())
    CA = input().strip(' ')
    QA = input().strip(' ')
    A = list(get())
    ANS.append(winnings(N, CA, QA, A))

for a in ANS:
    print(a)
