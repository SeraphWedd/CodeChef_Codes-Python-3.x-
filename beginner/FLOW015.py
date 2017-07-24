from calendar import weekday, day_name

ANS = []

T = int(input())

for l in range(T):
    ANS.append(day_name[weekday(int(input()), 1, 1)].lower())

for a in ANS:
    print(a)
