
mod = 10**9 + 7

def total_sum(l):
    total = 0
    factor = 2
    part = l.pop(0)<<1
    for v in l:
        total = (v*part + (total<<1))%mod
        part = (part + (v*factor))%mod
        factor = (factor<<1)%mod
    return total
    
def parse(val):
    return [int(value) for value in val.split(' ')]

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = parse(input())
        print(total_sum(A))
