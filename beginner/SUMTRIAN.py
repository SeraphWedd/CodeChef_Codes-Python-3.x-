
def triangles(arr):
    for row in range(len(arr)-2, -1, -1):
        #From second to the last line up to the 1st line
        #Backtracking from branches to root
        for col in range(len(arr[row])):
            arr[row][col] += max(arr[row+1][col:col+2])
            #Accumulative min/max tree
    return arr[0][0]
    
n = int(input())
for _ in range(n):
    l = int(input())
    arr = []
    for __ in range(l):
        arr.append([int(x) for x in input().strip(' ').split(' ')])
    print(triangles(arr))
