
def modulus(n, k):
    return (n%k == 0)

n, k = [int(x) for x in input().split(' ')]
ans = []
for l in range(n):
    if modulus(int(input()), k):
        ans.append(1)
print(len(ans))
