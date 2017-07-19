

def is_palindrome(arr):
    flip = [x for x in arr]
    flip.reverse()
    if arr == flip:
        return 'wins'
    else:
        return 'losses'

ANS = []

T = int(input().strip(' '))

for l in range(T):
    ANS.append(is_palindrome(list(map(int, input().strip(' ')))))

for l in ANS:
    print(l)
