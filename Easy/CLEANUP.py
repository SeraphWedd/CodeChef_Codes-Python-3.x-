
def clean(n, m, arr):
    d = {'c':[], 'a':[]}
    curr = 'c'
    r_item = ''
    
    try:
        r_item = arr.pop()
    except IndexError:
        pass
    
    for i in range(1, n+1):
        if i == r_item:
            try:
                r_item = arr.pop()
            except IndexError:
                r_item = ''
        else:
            d[curr].append(i)
            
            if curr == 'c':
                curr = 'a'
            else:
                curr = 'c'
                
    return d['c'], d['a']
            
            
    
ANS = []
T = int(input().strip(' '))

for l in range(T):
    N, M = map(int, input().strip(' ').split())
    ARR = list(map(int, input().strip(' ').split()))
    ARR.sort(reverse=True)
    ANS.append((clean(N, M, ARR)))

for c, a in ANS:
    print(' '.join(map(str, c)))
    print(' '.join(map(str, a)))
