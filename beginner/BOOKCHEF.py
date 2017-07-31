from heapq import heappush, heappop

N, M = map(int, input().split())
SPECIAL = list(input().split())

QUEUE = []
SP_QUEUE = []

for _ in range(M):

    f, p, s = input().split()

    if f in SPECIAL:
        heappush(SP_QUEUE, (-int(p), s))

    else:
        heappush(QUEUE, (-int(p), s))
        
for line in range(len(SP_QUEUE)):
    print(heappop(SP_QUEUE)[1])
    
for line in range(len(QUEUE)):
    print(heappop(QUEUE)[1])
