
def iterate(n, x, y):
    dic = {'xy':0, 'yx':0}
    for i in range(n):
        if i%2 == 0:
            dic['xy'] += x[i]
            dic['yx'] += y[i]
        elif i%2==1:
            dic['xy'] += y[i]
            dic['yx'] += x[i]
    return min(dic.values())
    
ANS = []

T = int(input())

for l in range(T):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    ANS.append(iterate(N, X, Y))

for a in ANS:
    print(a)
