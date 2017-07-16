def Z(n):
    count = 0
    while n >= 5:
        n //=5
        count += n
    return count

T = int(input())

for l in range(T):
    print(Z(int(input())))
