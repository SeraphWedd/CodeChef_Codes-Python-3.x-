
def countchef(s):
    c, h, e, f = 0, 0, 0, 0
    for char in s:
        if char == 'C':
            c += 1
        elif char == 'H':
            if c > h:
                h += 1
        elif char == 'E':
            if h > e:
                e += 1
        elif char == 'F':
            if e > f:
                f += 1
    return min(c, h, e, f)
print(countchef(input()))
