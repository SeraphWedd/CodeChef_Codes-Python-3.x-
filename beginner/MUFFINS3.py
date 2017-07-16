##def is_prime(n):
##    if n in [2, 3, 5, 7, 11]:
##        return True
##
##    elif n%2 == 0:
##        return False
##
##    else:
##        cnt = 0
##        for x in range(3, n//2, 2):
##            if n % x == 0:
##                cnt += 1
##        if cnt == 0:
##            return True
##        else:
##            return False
        
def greatest_div(n):
    if n%2 == 0:
        return (n/2)+1
    else:
        return (n+1)/2

T = int(input())
for l in range(T):
    N = int(input())
    print(int(greatest_div(N)))
    
