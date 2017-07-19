
ANS = []
def is_valid(arr):
    for x in arr:
        if (x <= 0) or (x > 180):
            return "NO"
        
    if sum(arr) == 180:
        return "YES"
    
    else:
        return "NO"
        

T = int(input())

for l in range(T):
    ANS.append(is_valid(list(map(int, input().strip(' ').split()))))

for a in ANS:
    print(a)
