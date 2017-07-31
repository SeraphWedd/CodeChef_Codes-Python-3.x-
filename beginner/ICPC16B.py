
def bea(n, a):
    #If there are 2 or more numbers with absolute value
    #greater than 1 return 'no' as the product will lead to
    #an infinite loop of checking (a*b = c, c*a = d, c*b=e, d*a=f etc.)
            
    #If there's only 1 with absolute value greater than 1 and there's
    #presence of -1, return 'no' (a*-1 = -a but -a is not in array
 
    #If theres more than one appearance of -1 and no one, return 'no'
    #(-1*-1=1 and there's no 1 in array)
 
    #If it wasn't caugth by any of the said cases, return 'yes'
    d = {'0':0, '1':0, '-1':0, 'other':0}
    for x in a:
        try:
            d[x] += 1
        except KeyError:
            d['other'] += 1
            if d['other'] > 1:
                return 'no'

    if (d['other']==1 and d['-1']>0) or (d['-1']>1 and d['1']==0):
        return 'no'
    else:
        return 'yes'
    
ANS = []

T = int(input())

for l in range(T):
    N = int(input())
    A = input().split()
    ANS.append(bea(N, A))

for a in ANS:
    print(a)
