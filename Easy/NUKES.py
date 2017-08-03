
A, N, K = map(int, input().split())
arr = [0 for x in range(K)]
for i in range(K):
    arr[i] = (A//((N+1)**(i)))%(N+1)

print(' '.join(map(str, arr)))
