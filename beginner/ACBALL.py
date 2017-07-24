

def hamming(x, y):
    ans = ''
    for i in range(len(x)):
        if x[i] == y[i]:
            if x[i] == 'W':
                ans += 'B'
            elif x[i] == 'B':
                ans += 'W'
        else:
            ans += 'B'
    return ans
    
ANS = []

T = int(input())

for l in range(T):
    X = input()
    Y = input()
    ANS.append(hamming(X, Y))

for a in ANS:
    print(a)
    
