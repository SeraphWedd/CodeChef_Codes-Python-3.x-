

def is_indian(string):
    if string.find('Y') != -1:
        return 'NOT INDIAN'
    elif string.find('I') != -1:
        return 'INDIAN'
    else:
        return 'NOT SURE'

ANS = []

T = int(input().strip(' '))

for l in range(T):
    N = int(input().strip(' '))
    ANS.append(is_indian(input()))

for a in ANS:
    print(a)
