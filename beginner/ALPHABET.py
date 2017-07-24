

def read(ms, ss):
    for c in ss:
        if c not in ms:
            return 'No'
    return 'Yes'

S = input()
N = int(input())
for l in range(N):
    W = input()
    print(read(S, W))
    
