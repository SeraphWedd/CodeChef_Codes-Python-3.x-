
def F(s):
    b = 0
    mb = 0
    for i in range(len(s)):
        if s[i] == '(':
            b += 1
        elif s[i] == ')':
            b -= 1
        mb = max(mb, b)
    return mb


ANS = []

T = int(input())

for l in range(T):
    n = F(input())
    string = '('*n + ')'*n
    ANS.append(string)

for a in ANS:
    print(a)
