
get = lambda: map(int, input().split())

def sick(a, b):
    an = ['Limak', 'Bob']
    at = [b, a]
    ac = [0, 0]
    for x in range(1, 1000):
        i = x%2
        if ac[i]+(x) > at[i]:
            return an[i]
        else:
            ac[i] += x

ANS = []

T = int(input())



for l in range(T):
    a, b = get()
    ANS.append(sick(a, b))

for a in ANS:
    print(a)
