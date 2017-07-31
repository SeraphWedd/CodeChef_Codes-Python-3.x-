
def parse(n, arr, c_num):
    A = [0 for x in range(n)]
    B = [0 for x in range(n)]
    for i in range(n):
        A[i] = arr[i]&65535 # 1<<16 -1
        B[i] = arr[i]>>16
    return A, B, c_num
        
    
ANS = []

T = int(input())

for l in range(T):
    N = int(input())
    ARR = [0 for x in range(N)]
    for i in range(N):
        ARR[i] = int(input())
    ANS.append(parse(N, ARR, l+1))

for A, B, c_num in ANS:
    print('Case %i:' %c_num)
    print(' '.join(map(str, A)))
    print(' '.join(map(str, B)))
    
    
