
N = int(input().strip(' '))
ARR = list(map(int, input().strip(' ').split()))

cnt = 0
for x in ARR:
    if x%2 == 0:
        cnt += 1

if cnt > N - cnt:
    print('READY FOR BATTLE')

else:
    print('NOT READY')
