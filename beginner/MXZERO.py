
get = lambda: map(int, input().split())

def mini(arr):
    zero = arr.count(0)
    one = arr.count(1)
    
    if one%2 != 0:
        return one
    else:
        return zero
        
ANS = []

T = int(input())

for l in range(T):
    N = int(input())
    ARR = list(get())
    ANS.append(mini(ARR))

for a in ANS:
    print(a)
