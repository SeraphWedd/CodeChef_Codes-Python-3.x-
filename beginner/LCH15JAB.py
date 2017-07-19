letters = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()

def counter(s):
    ans = []
    for l in letters:
        n = s.count(l)
        if n != 0:
            ans.append(n)

    if sum(ans) - max(ans) == max(ans):
        return 'YES'
    else:
        return 'NO'

ANS = []

T = int(input().strip(' '))

for l in range(T):
    str1 = input()
    ANS.append(counter(str1))

for a in ANS:
    print(a)
