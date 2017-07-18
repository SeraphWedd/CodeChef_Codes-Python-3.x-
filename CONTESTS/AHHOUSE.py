#Completed 07/18/2017

def min_pt(path, pt):
    t = 0
    for c in path:
        try:
            x, y = c
            t = t + pt[y][x]
        except TypeError:
            a, b = c
            t += min(min_pt(a, pt), min_pt(b, pt))
        else:
            continue
        
    return t

def min_pf(mat, N, M):
    path = [[0 for x in range(M)] for y in range(N)]
    s = [[x for x in y] for y in mat]

    for x in range(M):
        for y in range(N):
            if x == 0:
                if y == 0:
                    path[0][0] = [(x, y)]
                else:
                    s[y][x] = s[y][x] + s[y-1][x]
                    path[y][x] = path[y-1][x]+[(x,y)]

            elif y == 0:
                s[y][x] = s[y][x] + s[y][x-1]
                path[y][x] = path[y][x-1]+[(x,y)]

            else:
                a = s[y-1][x]
                b = s[y][x-1]
                if a<b:
                    s[y][x] = s[y][x] + a
                    path[y][x] = path[y-1][x]+[(x,y)]
                elif b<a:
                    s[y][x] = s[y][x] + b
                    path[y][x] = path[y][x-1]+[(x,y)]
                else:
                    s[y][x] = s[y][x] + a
                    path[y][x] = [(path[y-1][x]+[(x,y)],
                                   path[y][x-1]+[(x,y)])]

    return path[N-1][M-1], s[N-1][M-1]       
        

ANS = []

T = int(input())

for l in range(T):
    N, M = map(int, input().split(' '))
    mat_pf = [[0] for y in range(N)]
    mat_pt = [[0] for y in range(N)]
    
    for a in range(N):
        mat_pf[a] = list(map(int, input().split(' ')))

    for a in range(N):
        mat_pt[a] = list(map(int, input().split(' ')))
        
    paths, mnf = min_pf(mat_pf, N, M)
    mnt = min_pt(paths, mat_pt)
    ANS.append((mnf, mnt))

for a, b in ANS:
    print(a, b)
    

##
##Input:
##2
##2 2
##1 2
##3 4
##2 3
##1 4
##2 2
##1 2
##2 4
##2 1
##3 4
##Output:
##7 9
##7 7
##
