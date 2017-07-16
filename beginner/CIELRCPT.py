
def compute(n):
    i = 0
    while n >= (1<<(i+1)) and i < 11:
        i += 1
    return power2(n, i)

def power2(num, deg):
    while num > 0:
        x = (1<<deg)
        return (num//x) + power2(num%x, deg-1)
    return 0

T = int(input())

for l in range(T):
    p = int(input())
    print(compute(p))
