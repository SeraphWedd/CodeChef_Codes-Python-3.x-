
def evaluate(o, acts):
    laddus = 0
    for line in acts:
        a = line[0]
        if a == 'CONTEST_WON':
            laddus += 300
            b = int(line[1])
            if b < 20:
                laddus += (20 - b)
                
        elif a == 'TOP_CONTRIBUTOR':
            laddus += 300
            
        elif a == 'BUG_FOUND':
            laddus += int(line[1])

        elif a == 'CONTEST_HOSTED':
            laddus += 50
    if o == 'INDIAN':
        return laddus//200
    else:
        return laddus//400
    
ANS = []

T = int(input())

for l in range(T):
    raw = input().split()
    act = int(raw[0])
    ori = raw[1]
    li = []
    for _ in range(act):
        li.append(input().split())
    ANS.append(evaluate(ori, li))

for a in ANS:
    print(a)
