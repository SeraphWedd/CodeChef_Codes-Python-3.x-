
from collections import deque

mod = 1000000007

def minArray(a, n, k):
    end = deque()
    end.append(0)
    for x in range(1, n):
        
        while end[0] < x - k: #This function accumulates a list of k elements
            end.popleft() #removes the oldest elements
            
        a[x] *= a[end[0]] #Rewrites a[x] into the optimized product
        
        while end and a[end[-1]] >= a[x]:
            #If end is not empty and its last element is >= to a[x]
            end.pop()
        end.append(x)
        
    print(a[-1]%mod)
    
def parse(val):
    return [int(value) for value in val.split(' ')]

if __name__ == "__main__":
    
    N, K = parse(input())
    A = parse(input())
    minArray(A, N, K)
