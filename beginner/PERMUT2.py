

#Global
ANS = []

def check_inv(arr):
    l = len(arr)
    t = [0]*l
    for i in range(l):
        t[arr[i]-1] = i+1

    for i in range(l):
        if arr[i] != t[i]:
            ANS.append('not ambiguous')
            return
    ANS.append('ambiguous')
        
while True:
    n = int(input())
    if n == 0:
        break
    arr = [int(x) for x in input().split(' ')]
    check_inv(arr)

for line in ANS:
    print(line)
