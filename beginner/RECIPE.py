##
##Input
##
##Input will begin with an integer T, the number of test cases.
##Each test case consists of a single line. The line begins with
##a positive integer N, the number of ingredients. N integers follow,
##each indicating the quantity of a particular ingredient that is used.
##
##Output
##
##For each test case, output exactly N space-separated integers on a line,
##giving the quantity of each ingredient that the chef should use in order
##to make as little food as possible.
##
##Constraints
##
##T≤100
##2≤N≤50
##All ingredient quantities are between 1 and 1000, inclusive.
##
##Sample Input
##
##3
##2 4 4
##3 2 3 4
##4 3 15 9 6
##
##Sample Output
##
##1 1
##2 3 4
##1 5 3 2
##

def get_gcf(arr):
    temp = [x for x in arr]
    for  i in range(len(arr)-1):
        a = temp[i]
        b = temp[i+1]
        result = gcf(a, b)
        
        if result == 1:
            return 1
        
        temp[i+1] = result    
    return temp[-1]

def gcf(x, y):
    large = max(x, y)
    small = min(x, y)
    r = 1
    while r:
        r = large%small
        if r != 0:
            large = small
            small = r
    return small
    
ANS = []

T = int(input())

for l in range(T):
    arr = list(map(int, input().strip(' ').split(' ')))
    ANS.append((get_gcf(arr[1:]), arr[1:]))

for line in ANS:
    a = []
    d = line[0]
    for var in line[1]:
        a.append(var//d)
    print(' '.join(map(str, a)))
