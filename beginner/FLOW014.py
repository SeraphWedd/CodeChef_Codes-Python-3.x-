
def grade(h, c, t):
    ans = [0, 0, 0]
    if h > 50:
        ans[0] = 1
    if c < 0.7:
        ans[1] = 1
    if t > 5600:
        ans[2] = 1

    cnt = ans.count(1)
    if cnt == 3:
        return 10
    elif cnt == 1:
        return 6
    elif cnt == 0:
        return 5
    elif ans[0] and ans[1]:
        return 9
    elif ans[1] and ans[2]:
        return 8
    elif ans[0] and ans[2]:
        return 7
    
    

ANS = []

T = int(input().strip(' '))

for l in range(T):
    h, c, t = map(float, input().strip(' ').split())
    ANS.append(grade(h, c, t))

for a in ANS:
    print(a)
