
def elect(a):
    s = a.count('s')
    m = a.count('m')
    
    sub = 0

    t = a + '!'
    while t[0] != '!':
        try:
            if t[0] == 's':
                t = t[t.index('m')+1:]
                sub += 1
            elif t[0] == 'm':
                t = t[t.index('s')+1:]
                sub += 1
        except ValueError:
            t = '!'
            
    s -= sub
    
    if s == m:
        return 'tie'
    elif s > m:
        return 'snakes'
    elif s < m:
        return 'mongooses'
        


T = int(input())

for l in range(T):
    print(elect(input()))
