

def ship_class(ID):
    c = ID.lower()
    if c == 'b':
        return 'BattleShip'
    elif c == 'c':
        return 'Cruiser'
    elif c == 'd':
        return 'Destroyer'
    elif c == 'f':
        return 'Frigate'

ANS = []

T = int(input().strip(' '))

for l in range(T):
    ANS.append(ship_class(input().strip(' ')))

for a in ANS:
    print(a)
    
