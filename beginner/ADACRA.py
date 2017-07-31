
def counter(string):
    d = {'U':0, 'D':0}
    
    prev = string[0]
    l = len(string)
    
    for i in range(1, l):
        if prev != string[i]:
            d[prev] += 1
            prev = string[i]
    d[prev] += 1
    
    return min(d.values())

ANS = []
T = int(input())

for l in range(T):
    ANS.append(counter(input()))

for a in ANS:
    print(a)
