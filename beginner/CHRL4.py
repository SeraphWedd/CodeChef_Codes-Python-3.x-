from math import log
from heapq import heappop, heappush

mod = 1000000007

def minArray(a, n, k):
    s = [x for x in a]
    q = []
    heappush(q, (log(s[0]), 0))
    
    for i in range(1, n):
        
        v, ind = heappop(q)
        
        while k < i - ind: #This function accumulates a list of k elements
            v, ind = heappop(q)
            
        s[i] = (s[ind]*a[i]) % mod#Rewrites s[i] into the optimized product
        
        heappush(q, (v, ind))
        heappush(q, (v+log(a[i]), i))
        
    return s[-1]

N, K = map(int, input().split(' '))
A = list(map(int, input().split(' ')))
print(minArray(A, N, K))

