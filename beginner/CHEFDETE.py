
N = int(input())
ARR = set(list(map(int, input().split())))
temp = {a for a in range(1, N+1)}
ans = sorted(temp - ARR)
print(' '.join(map(str, ans)))
